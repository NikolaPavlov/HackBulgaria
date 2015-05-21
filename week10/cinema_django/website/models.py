from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField()

    def __str__(self):
        return '{}'.format(self.name)


class Projection(models.Model):
    movie_id = models.ForeignKey(Movie)
    type_projection = models.CharField(max_length=4)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return '{} - {} -{} - {}'.format(
            self.movie_id, self.type_projection,
            self.date, self.time)


class Reservation(models.Model):
    username = models.CharField(max_length=30, unique=True)
    projection_id = models.ForeignKey(Projection)
    row = models.IntegerField()
    col = models.IntegerField()

    def __str__(self):
        return '{} - {} - {} - {}'. format(
            self.username, self.projection_id,
            self.row, self.col)
