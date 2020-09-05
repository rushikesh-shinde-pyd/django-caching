from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=20)
    artist = models.CharField(max_length=20)


    def __str__(self):
        return self.name