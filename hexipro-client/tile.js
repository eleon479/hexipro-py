
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

}