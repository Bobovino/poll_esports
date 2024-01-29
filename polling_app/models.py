from django.db import models

class RegionsModel(models.Model):
    region = models.CharField(max_length=100)