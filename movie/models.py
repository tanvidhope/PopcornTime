from django.db import models
# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=1000)
    score = models.FloatField()
    popularity = models.FloatField()
    url=models.CharField(max_length=1000, default='')
    img = models.CharField(max_length=1000, default='')
    adventure_genre = models.BooleanField(default=False)
    comedy_genre = models.BooleanField(default=False)
    thriller_genre = models.BooleanField(default=False)
    action_genre = models.BooleanField(default=False)
    romance_genre = models.BooleanField(default=False)
    animation_genre = models.BooleanField(default=False)
    def __str__(self):
        return self.title
