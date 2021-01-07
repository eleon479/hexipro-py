class Board {
    constructor(rows, columns) {
        console.log("creating board")
        this.rows=rows
        this.columns=columns
        this.tiles=this.createTiles(rows, columns)
        console.log(this.getTile(4,3))
        this.populateTiles()
    }

    getRows() {
      return this.rows
    }

    getColumns() {
      return this.columns
    }

    setRows(rows) {
      this.rows=rows
    }
    
    setColumns(columns) {
      this.columns=columns
    }

    //creates empty default tiles
    createTiles(rows, columns) {
        
        var tiles=[] 
        var count=0
        var currTile
      for(var i=0; i<columns; i++) {

        for(var j=0; j<rows; j++) {
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
      var tile=this.getTile(6,6)
      this.stealTile(player, tile)
      console.log(tile.getPlayerOnTile())
      console.log("Player can attack: " + tile.getAttackableTiles())
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