from django.db import models

from hexipro.players.models import Player


class Board(models.Model):

    Turn = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        null=True,
        related_name="board_turn",
    )
