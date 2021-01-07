from .models import Player, Board, Tile
import random

def allocate(player_name, col, row):
    if Tile.objects.get(row=row, column=col).owner==Player.objects.get(name=player_name):
        Tile.objects.get(row=row, column=col).power += 1
        Tile.objects.get(row=row, column=col).save()

def move(player_name, startCol, startRow, endCol, endRow):
    if Tile.objects.get(row=startCol, col=endCol).owner==Player.objects.get(name=player_name):
        startPower = Tile.objects.get(row=startRow, col=startCol).power
        endPower = Tile.objects.get(row=endRow, col=endCol)

        if (startPower < 2): 
            return ["reject " + player_name + " " + startCol + " " + startRow]

        difference = startPower - endPower
        if (difference < -1):
            return fail(player_name, startCol, startRow, endCol, endRow)
        elif (difference == -1):
            if (random.randint(0,3) == 0):
                return win(player_name, startCol, startRow, endCol, endRow)
            else:
                return fail(player_name, startCol, startRow, endCol, endRow)
        elif (difference == 0):
            if (random.randint(0,1) == 0):
                return win(player_name, startCol, startRow, endCol, endRow)
            else:
                return fail(player_name, startCol, startRow, endCol, endRow)
        elif (difference == 1):
            if (random.randint(0,3) != 0):
                return win(player_name, startCol, startRow, endCol, endRow)
            else:
                return fail(player_name, startCol, startRow, endCol, endRow)
        elif (difference > 1):
            return kill(player_name, startCol, startRow, endCol, endRow, difference)

def fail(player_name, startCol, startRow, endCol, endRow):
    Tile.objects.get(row=startRow, col=startCol).power = 1
    Tile.objects.get(row=startRow, col=startCol).save()
    return ["tile " + player_name + " " + startCol + " " + startRow + " 1"]

def win(player_name, startCol, startRow, endCol, endRow):
    Tile.objects.get(row=startRow, col=startCol).power = 1
    Tile.objects.get(row=startRow, col=startCol).save()

    Tile.objects.get(row=startRow, col=startCol).power = 1
    Tile.objects.get(row=startRow, col=startCol).owner = Player.objects.get(name=player_name)
    Tile.objects.get(row=startRow, col=startCol).save()

    return ["tile " + player_name + " " + startCol + " " + startRow + " 1",
    "tile " + player_name + " " + endCol + " " + endRow + " 1"]

def kill(player_name, startCol, startRow, endCol, endRow, difference):
    Tile.objects.get(row=startRow, col=startCol).power = 1
    Tile.objects.get(row=startRow, col=startCol).save()

    Tile.objects.get(row=startRow, col=startCol).power = difference
    Tile.objects.get(row=startRow, col=startCol).owner = Player.objects.get(name=player_name)
    Tile.objects.get(row=startRow, col=startCol).save()

    return ["tile " + player_name + " " + startCol + " " + startRow + " 1",
    "tile " + player_name + " " + endCol + " " + endRow + " " + difference]


        


        