from django.db import models


class emp(models.Model):
    name = models.CharField(max_length=20)
    sal = models.FloatField()
