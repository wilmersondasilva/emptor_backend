import csv
import os

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from api.models import Country,  Indicator, Value

DATA_SOURCES_DIR = os.path.join(settings.BASE_DIR, 'api/data_sources')


class Command(BaseCommand):
    help = 'Populate the API database'

    def handle(self, *args, **options):
        countries = []
        indicators = []

        with open(f"{DATA_SOURCES_DIR}/population_total.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    self.stdout.write(f'Column names are {", ".join(row)}')
                    line_count += 1
