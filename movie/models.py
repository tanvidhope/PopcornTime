from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=1000)
    score = models.FloatField()
    popularity = models.FloatField()

    def __str__(self):
        return self.name
