
class Tile {
    constructor(location, playerOnTile, valueOnTile /*,isActive*/ ) {
        this.location=location
        this.playerOnTile=playerOnTile
        this.valueOnTile=valueOnTile
        //this.isActive=this.isActive
    }

    setPlayerOnTile(player) {
        this.playerOnTile=player
    }
    
    setValueOnTile (newVal) {
        this.valueOnTile=newVal
    }

    getLocation () {
        return this.location
    }
    /*
    setIsActive (active) {
        //active=true -> tile is in play
        this.isActive=active
    }
    */

    getPlayerOnTile() {
        return this.playerOnTile
    }

    getValueOnTile() {
        return this.valueOnTile
    }

    getAttackableTiles() {
        var loc=this.getLocation()
        var row=loc[0]
        var column=loc[1]
        var rows=12
        var columns=7
        var attackableTiles=[]

        //first tile
        if((row==0) & (column==0)) {
            attackableTiles[attackableTiles.length]=[row, column-1]
            attackableTiles[attackableTiles.length]=[row+1, column+1]
        }
       return attackableTiles
    }
}