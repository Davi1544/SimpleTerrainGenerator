from random import randint
from tile import Tile
import math

class Cell:
    def __init__(self,
                position : tuple = (0,0),
                tileId : str = "",
                fittingSockets : dict[str, set[str]] = {}
                ):
        
        self.position = position
        self.tileId = tileId
        self.fittingSockets = fittingSockets
        self.possibleTileIds = set()
        self.entropy = 0

    def __str__(self):
        if self.tileId != "0":
            text = f"Cell Object on coordinates ({self.position[0]},{self.position[1]}) assigned with tile id {self.tileId}"
        else:
            text = f"Cell Object on coordinates ({self.position[0]},{self.position[1]}) with entropy = {self.entropy} and possible tiles {self.possibleTileIds}. This cell has the following fitting sockets : {self.fittingSockets}"
        return text


    # filter que possible tiles based on the sockets
    def filterTiles(self, tiles : list[Tile]):
        if self.tileId != "0": return
        self.possibleTileIds = set()

        # filtering possible tiles based on the available sockets for each position
        for tile in tiles:
            allowTile = True
            for socketPosition in tile.sockets:
                if not(tile.sockets[socketPosition] in self.fittingSockets[socketPosition]):
                    allowTile = False
                    break
            
            if allowTile:
                self.possibleTileIds.add(tile.id)

    
    def setTile(self, tiles : dict[str, Tile], tileId : str):
        self.tileId = tileId
        self.fittingSockets = tiles[tileId].sockets

    def selectRandom(self, tiles : dict[str, Tile]):
        weights : dict[str, int] = {}
        weightSum = 0

        # preparing selection of random tile based on weights
        for tileId in tiles:
            tile = tiles[tileId]
            if tile.id in self.possibleTileIds:
                weights[tile.id] = tile.weight
                weightSum = weightSum + tile.weight

        # selecting random tile
        randomInt = randint(0,weightSum)
        subTotal : int = 0
        for id in weights:
            subTotal += weights[id]
            if subTotal >= randomInt:
                self.setTile(tiles, id)
                break


        self.possibleTileIds = set()
        return
    
    def calculateFittingSockets(self, tiles : dict[str, Tile]):
        self.fittingSockets = {
            "N":set(),
            "E":set(),
            "S":set(),
            "W":set()
        }

        for tileId in self.possibleTileIds:
            tile = tiles[tileId]

            for direction in ["N","E","S","W"]:
                self.fittingSockets[direction] = self.fittingSockets[direction] | tile.sockets[direction]

    
    def calculatePossibleTileIds(self, tiles : dict[str, Tile]):
        possibleTileIdsCopy = self.possibleTileIds.copy()
        self.possibleTileIds = set()

        for tileId in possibleTileIdsCopy:
            tile = tiles[tileId]
            allowed = True
            for direction in ["N","E","S","W"]:
                if len(self.fittingSockets[direction] & tile.sockets[direction]) < 1:
                    allowed = False
                    break

            if allowed:
                self.possibleTileIds.add(tileId)

    def calculateEntropy(self, tiles : dict[str, Tile]):
        if self.possibleTileIds == set(): 
            self.entropy = 0
            return
        
        # else
        self.entropy = 0
        weightList = []
        for tileId in self.possibleTileIds:
            weightList.append(tiles[tileId].weight)

        totalWeights : int = sum(weightList)

        for tileId in self.possibleTileIds:
            self.entropy += - (tiles[tileId].weight/totalWeights)*math.log2(tiles[tileId].weight/totalWeights)