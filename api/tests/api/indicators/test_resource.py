from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Indicator


class TestGet(APITestCase):
    def test_list_all_indicators(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_that_it_returns_correct_data(self):
        indicator = Indicator.objects.create(
            indicator_name='Population',
            indicator_code='TOT.POP',
            country_name='Brazil',
            country_code='BRA',
            value='2323',
            year='1999'
        )

        response = self.client.get('/api/')

        self.assertListEqual(response.data, [{
            'id': indicator.id,
            'name': indicator.indicator_name,
            'code': indicator.indicator_code,
            'country_name': indicator.country_name,
            'country_code': indicator.country_code,
            'value': indicator.value,
            'year': indicator.year
        }])
