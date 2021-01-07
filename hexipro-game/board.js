class Board {
    constructor() {
        console.log("creating board")
        this.createTiles(4,4)
        this.populateTiles()
    }

    createTiles(rows, columns) {
        var tiles=[] 
        var count=0
        var currTile
      for(var i=0; i<columns; i++) {
          console.log("now on column" + i)
        for(var j=0; j<rows; j++) {
            console.log("now on row " + j)
            currTile=new Tile([i,j], 'none',0)
            tiles[count]=currTile
            count++
        }
      }

      //Complete Board is created and printed
      console.log(tiles)
    }

    populateTiles() {
        
    }
}