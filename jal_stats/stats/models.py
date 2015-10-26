from django.db import models

# Create your models here.


class Activity(models.Model):
    full_description = models.CharField(max_length=255)
    units = models.CharField(max_length=40)

    def __str__(self):
        return self.full_description


class Datapoint(models.Model):
    activity = models.ForeignKey('Activity')
    reps = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {} at {}'.format(self.reps,
                                    self.activity.units,
                                    self.timestamp)
