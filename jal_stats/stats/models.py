from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User

# Create your models here.


class Activity(models.Model):
    # user = models.ForeignKey(User)
    full_description = models.CharField(max_length=255)
    units = models.CharField(max_length=40)


    class Meta:
        default_related_name = 'activities'

    def __str__(self):
        return self.full_description


class Stat(models.Model):
    activity = models.ForeignKey('Activity')
    reps = models.PositiveIntegerField()
    date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['-date']
        unique_together = ('activity', 'date')

    def __str__(self):
        return '{} {} at {}'.format(self.reps,
                                    self.activity.units,
                                    self.date)
