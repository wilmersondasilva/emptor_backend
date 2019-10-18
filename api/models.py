from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)


class Indicator(models.Model):
    name = models.CharField(max_length=70)
    code = models.CharField(max_length=20)


class Value(models.Model):
    value = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE)
