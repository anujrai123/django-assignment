# pilotlog/models.py
from django.db import models

class Aircraft(models.Model):
    user_id = models.IntegerField()
    table = models.CharField(max_length=50)
    guid = models.CharField(max_length=36)
    meta = models.JSONField()
    platform = models.IntegerField()
    _modified = models.IntegerField()

    def __str__(self):
        return f'Aircraft - {self.guid}'

class Pilot(models.Model):
    user_id = models.IntegerField()
    table = models.CharField(max_length=50)
    guid = models.CharField(max_length=36)
    meta = models.JSONField()
    platform = models.IntegerField()
    _modified = models.IntegerField()

    def __str__(self):
        return f'Pilot - {self.guid}'

