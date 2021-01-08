
class Player {
    constructor(name, color, numTiles) {
        this.name=name
        this.color=color
        this.numTiles=numTiles
        
    }

    setName(name) {
        this.name=name
    }

    setColor(color) {
        this.color=color
    }

    setNumTiles(tiles) {
        this.numTiles=tiles
    }

    getName() {
        return this.name
    }

    getColor() {
        return this.color
    }

    getNumTiles() {
        return this.numTiles
    }
}