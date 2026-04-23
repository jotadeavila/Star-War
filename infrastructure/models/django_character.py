from django.db import models


class DjangoCharacter(models.Model):
    name = models.CharField(max_length=100)
    height = models.CharField(max_length=10, blank=True, null=True)
    mass = models.CharField(max_length=10, blank=True, null=True)
    hair_color = models.CharField(max_length=50, blank=True, null=True)
    skin_color = models.CharField(max_length=50, blank=True, null=True)
    eye_color = models.CharField(max_length=50, blank=True, null=True)
    birth_year = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    films = models.ManyToManyField('DjangoFilm', related_name='characters', blank=True)

    class Meta:
        db_table = 'characters'
        app_label = 'infrastructure'

    def __str__(self):
        return self.name