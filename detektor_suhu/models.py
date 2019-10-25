from django.db import models

# Create your models here.
class Stats(models.Model):
    temperature = models.fields.FloatField()
    humidity = models.fields.FloatField()
