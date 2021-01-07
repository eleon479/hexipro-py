from django.db import models

from hexipro.players.models import Player


class Tile(models.Model):

    row = models.IntegerField(default=0)

    column = models.IntegerField(default=0)

    owner = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        null=True,
        related_name="tile_owner",
    )

    power = models.IntegerField(default=0)

    active = models.BooleanField(default=True)
