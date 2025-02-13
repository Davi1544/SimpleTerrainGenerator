from random import randint
import math

class Cell:
    def __init__(self,
                position : list = [0,0],
                tile : int = 0,
                possibleTiles : set = {}
                ):
        
        self.position = position
        self.tile = tile
        self.possibleTiles = possibleTiles
        self.entropy = 0

    def __str__(self):
        if self.tile != 0:
            text = f"Cell Object on coordinates ({self.position[0]},{self.position[1]}) assigned with tile id {self.tile}"
        else:
            text = f"Cell Object on coordinates ({self.position[0]},{self.position[1]}) with entropy = {self.entropy} and possible tiles {self.possibleTiles}"
        return text
    
    def selectRandom(self, weightPerTile : dict):
        weightList = []
        ids : list = []
        for i in weightPerTile:
            if i in self.possibleTiles:
                weightList.append(weightPerTile[i])
                ids.append(i)

        totalWeights : int = sum(weightList)
        randomValue : int = randint(1, totalWeights)

        subTotal : int = 0
        for index in range(len(weightList)):
            subTotal += weightList[index]
            if subTotal >= randomValue:
                self.tile = ids[index]
                break

        self.possibleTiles = set()
        self.entropy = 0

    def calculateEntropy(self, weightPerTile : dict):
        if self.possibleTiles == set(): 
            self.entropy = 0
            return
        
        # else
        self.entropy = 0
        weightList = []
        for i in weightPerTile:
            if i in self.possibleTiles:
                weightList.append(weightPerTile[i])

        totalWeights : int = sum(weightList)

        for tile in self.possibleTiles:
            self.entropy += - (weightPerTile[tile]/totalWeights)*math.log2(weightPerTile[tile]/totalWeights)

