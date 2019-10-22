from django.db import models


class Indicator(models.Model):
    name = models.CharField(max_length=70)
    code = models.CharField(max_length=20)
    country_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=3)
    value = models.CharField(max_length=255, default='')
    year = models.CharField(max_length=4)

    class Meta:
        ordering = ['id']
