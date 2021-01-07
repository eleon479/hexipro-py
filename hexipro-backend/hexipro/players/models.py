from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=225)

    color = models.CharField(max_length=225)

    tile_count = models.IntegerField(default=0)

    def get_tile_count():
        return tile_count
