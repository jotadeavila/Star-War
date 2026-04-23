from django.db import models


class DjangoFilm(models.Model):
    title = models.CharField(max_length=200)
    episode_id = models.IntegerField(blank=True, null=True)
    opening_crawl = models.TextField(blank=True, null=True)
    director = models.CharField(max_length=100, blank=True, null=True)
    producer = models.CharField(max_length=200, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'films'
        app_label = 'infrastructure'

    def __str__(self):
        return self.title