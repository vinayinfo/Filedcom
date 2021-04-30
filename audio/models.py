from django.conf import settings
from django.db import models


class AudioBase(models.Model):
    uploaded_time = models.DateTimeField()
    duration_time = models.IntegerField(default=0)


class AudioBook(AudioBase):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)


class Podcast(AudioBase):
    name = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    participents = models.CharField(max_length=100)


class Song(AudioBase):
    name = models.CharField(max_length=100)