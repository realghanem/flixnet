from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateField()
    genre = models.CharField(max_length=300)
    duration = models.CharField(max_length=100)
    posterLink = models.TextField()
    videoLink = models.TextField()
    description = models.TextField()
    rating = models.CharField(max_length=10)

    def __str__(self):
        return self.title
