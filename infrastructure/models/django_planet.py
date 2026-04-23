from django.db import models


class DjangoPlanet(models.Model):
    name = models.CharField(max_length=100)
    climate = models.CharField(max_length=100, blank=True, null=True)
    terrain = models.CharField(max_length=100, blank=True, null=True)
    population = models.CharField(max_length=50, blank=True, null=True)
    gravity = models.CharField(max_length=50, blank=True, null=True)
    diameter = models.CharField(max_length=50, blank=True, null=True)
    films = models.ManyToManyField('DjangoFilm', related_name='planets', blank=True)

    class Meta:
        db_table = 'planets'
        app_label = 'infrastructure'

    def __str__(self):
        return self.name