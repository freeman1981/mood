from django.db import models
from django.contrib.auth.models import User


class Mood(models.Model):
    mood_value = models.ForeignKey('MoodValues')
    datetime = models.DateTimeField('DateTime')
    owner = models.ForeignKey(User)

    def __str__(self):
        return '/'.join((self.mood_value.description, self.owner.username, str(self.datetime)))


class MoodValues(models.Model):
    description = models.CharField('Description', max_length=256)
    value = models.IntegerField('Mood_value')

    def __str__(self):
        return self.description
