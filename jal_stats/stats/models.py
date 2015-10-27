from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User

# Create your models here.


class Activity(models.Model):
    # user = models.ForeignKey(User, related_name='activities')
    full_description = models.CharField(max_length=255)
    units = models.CharField(max_length=40)

    def __str__(self):
        return self.full_description


class Datapoint(models.Model):
    activity = models.ForeignKey('Activity')
    reps = models.PositiveIntegerField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return '{} {} at {}'.format(self.reps,
                                    self.activity.units,
                                    self.date)
