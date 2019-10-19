import csv
import os
import glob

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db import transaction

from api.models import Indicator

DATA_SOURCES_DIR = os.path.join(settings.BASE_DIR, 'api/data_sources')


class Command(BaseCommand):
    help = 'Populate the API database'

    def handle(self, *args, **options):
        self.stdout.write('Starting... ')

        try:
            with transaction.atomic():
                for filename in glob.glob(f'{DATA_SOURCES_DIR}/*.csv'):
                    with open(filename, mode='r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        years = []

                        self.stdout.write(f'Start getting data from {filename}')
                        for index_row, row in enumerate(csv_reader):
                            year_columns = range(4, len(row) - 1)

                            if index_row == 0:
                                for column in year_columns:
                                    years.append(row[column])
                            else:
                                for index_year, column in enumerate(year_columns):
                                    indicator = {
                                        'country_name': row[0],
                                        'country_code': row[1],
                                        'name': row[2],
                                        'code': row[3],
                                        'value': row[column],
                                        'year': years[index_year]
                                    }

                                    Indicator.objects.create(**indicator)

                        self.stdout.write(self.style.SUCCESS(f'{filename} data saved into database successfully!'))

            self.stdout.write('Finished!')
        except:
            if options['traceback']:
                raise
            else:
                raise CommandError("Something wrong has happened and the database wasn't populated. "
                                   "Try run using the argument --traceback for more info.")
