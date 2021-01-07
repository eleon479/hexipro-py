from .models import Player, Board, Tile

def allocate(player_name, col, row):
    if Tile.objects.get(row=row, column=col).owner==Player.objects.get(name=player_name):
        Tile.objects.get(row=row, column=col).power += 1
        Tile.objects.get(row=row, column=col).save()

def move(player_name, startCol, startRow, endCol, endRow):
    if Tile.objects


        