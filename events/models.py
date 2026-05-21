from django.db import models

class Event(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    date = models.DateField()

    seats = models.IntegerField()

    image = models.URLField()

    def __str__(self):
        return self.title