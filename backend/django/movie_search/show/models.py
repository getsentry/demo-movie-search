from operator import index
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200, unique=True, db_index=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Show(models.Model):
    show_type = models.CharField(max_length=200, db_index=True)
    title = models.CharField(max_length=200, db_index=True)
    countries = models.CharField(max_length=200)
    date_added = models.CharField(max_length=200)
    release_year = models.SmallIntegerField()
    rating = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    categories = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    director = models.ManyToManyField(Person, related_name="director_in")
    cast = models.ManyToManyField(Person, related_name="cast_in")

    class Meta:
        ordering = ("title",)
