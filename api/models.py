from django.db import models

class Indicator(models.Model):
    indicator_name = models.CharField(max_length=70)
    indicator_code = models.CharField(max_length=20)
    country_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=3)
    value = models.CharField(max_length=255, default='')
    year = models.CharField(max_length=4)