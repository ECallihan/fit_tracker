from django.db import models
from django.conf import settings

import datetime


# Create your models here.


class Technique(models.Model):
    tech_id = models.AutoField(primary_key=True)
    technique_name = models.TextField()
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    for_strength = models.BooleanField()
    for_cardio = models.BooleanField()
    for_flexibility = models.BooleanField()
    has_time = models.BooleanField()
    has_resistance = models.BooleanField()
    has_reps = models.BooleanField()


class Entry(models.Model):
    entry_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    entry_date = models.DateField()
    entry_notes = models.TextField()


class Exercise(models.Model):
    exercise_id = models.AutoField(primary_key=True)
    entry_id = models.ForeignKey(Entry, on_delete=models.CASCADE)
    technique_id = models.ForeignKey(Technique, on_delete=models.CASCADE)


class Exercise_Set(models.Model):
    exercise_set_id = models.AutoField(primary_key=True)
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    set_number = models.IntegerField()
    rep_count = models.IntegerField()
    weight = models.IntegerField()
    duration = models.DurationField()
