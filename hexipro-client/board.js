class Board {
    constructor() {
        console.log("creating board")
        this.tiles=this.createTiles(12,7)
        console.log(this.getTile(4,3))
        this.populateTiles()
    }

    //creates empty default tiles
    createTiles(rows, columns) {
        
        var tiles=[] 
        var count=0
        var currTile
      for(var i=0; i<columns; i++) {
          console.log("now on column" + i)
        for(var j=0; j<rows; j++) {
            console.log("now on row " + j)
            currTile=new Tile([i,j], null,0)
            tiles[count]=currTile
            count++
        }
      }

      //Complete Board is created and printed
      console.log(tiles)
      return tiles
    }

    //place player on start tiles
    populateTiles() {
      var player=new Player('player','green',1)
      var tile=this.getTile(0,0)
      this.stealTile(player, tile)
      console.log(tile.getPlayerOnTile())
    }

    stealTile(player, tile) {
      tile.setPlayerOnTile(player)
    }
    
    //to get player on tile: getTile.getPlayerOnTile
    //to get value on tile: getTile.getValueOnTile
    getTile(row, column) {
      return this.tiles[((12*row))+(column)]
    }


}