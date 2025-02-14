from SimpleTerrainGenerator.simple.cell import *
from random import randint
import time
import os
from PIL import Image
import numpy as np

# sample
import SimpleTerrainGenerator.simple.sample1 as smp

########################
# 
# STEPS
#
# 1. Define the tiles, their respective ids and additional information
# 2. Define the rules for neighboring tiles for each tile
# 3. Define the weight for each tile
# 4. Make an MN list of cell objects with no tile
# 5. Make an empty MN list of cells that are filled
# 6. Fill the list of assigned cells while emptying the list of unassigned cells
#   6.1. Choose a cell 
#       6.1.1. Choose a random cell (first iteration)
#       6.1.2. Choose the cell with the least entropy (other iterations)
#   6.2. Fill it using its "tileOptions" list
#   6.3. Move the cell to the assigned cell list
#   6.4. Propagate the necessary information to its neighboring cells
#   6.5. If necessary, propagate again and again until all cells have been updated
#       6.5.1. This can be done by keeping a list of cells that were affected by a propagation and then propagating on them
#   6.6. Rinse and repeat  
# 7. Convert the filled list into an M by N image

def printBoardCells(board : dict[tuple, Cell] = {}, M : int = 10, N : int = 10):
    for i in range(M):
        for j in range(N):
            print(f"{i,j}: {board[(i,j)]}")

def printBoard(board : dict[tuple, Cell] = {}, M : int = 10, N : int = 10):
    for i in range(M):
        for j in range(N):
            print(f"{smp.emojiMap[board[(i,j)].tile]}",end="")
        print()

def getAcceptableNeighbors(neighbors : dict[int, set], source : Cell):

    if (source.tile in neighbors) and (source.tile != 0):
        return neighbors[source.tile]
    
    if source.tile == 0:
        res = set()
        for possibleTile in source.possibleTiles:
            res = res | neighbors[possibleTile] if possibleTile in neighbors else {}
        
        return res
    
def propagate(weights : dict[int, int], 
              neighbors : dict[int, set], 
              board : dict[tuple, Cell], 
              source : Cell):
    acceptableNeighbors : set = getAcceptableNeighbors(neighbors, source)
    i, j = source.position 
    affectedCells : list[Cell] = []

    neighborPositions = [
        (i-1, j),
        (i, j-1),
        (i+1, j),
        (i, j+1)
    ]

    for neighborPosition in neighborPositions:
        if neighborPosition in board:
            neighborCell = board[neighborPosition]
            commonTiles = neighborCell.possibleTiles & acceptableNeighbors
            
            if not(neighborCell.possibleTiles == commonTiles) and neighborCell.tile == 0:
                affectedCells.append(neighborCell)
                neighborCell.possibleTiles = commonTiles
                neighborCell.calculateEntropy(weights)

    for affectedNeighborCell in affectedCells:
        propagate(weights, neighbors, board, affectedNeighborCell)
    

# main function
def main(M : int, N : int, timeLapse : bool = False) -> None:

    # 1., 2. and 3. are all contained in the sample file
    # 4., 5.
    board : dict[tuple, Cell]= {}
    assignedList : list[Cell] = []
    unassignedList : list[Cell] = []

    for i in range(M):
        for j in range(N):
            cell = Cell([i,j], 0, possibleTiles=set(range(1,len(smp.weights))))
            cell.calculateEntropy(smp.weights)
            board[(i,j)] = cell
            unassignedList.append(cell)
    
    
    # 6.
    # 6.1.1.
    randIndex : int = randint(0,M*N - 1)
    firstCell : Cell = unassignedList[randIndex]
    assignedList.append(firstCell)
    del unassignedList[randIndex]
    firstCell.selectRandom(smp.weights)

    propagate(smp.weights, smp.neighbors, board, firstCell)

    while len(unassignedList) > 0:
        leastEntropyCell : Cell = unassignedList[0]
        leastEntropyCellIndex = 0
        for cellIndex in range(len(unassignedList)):
            if unassignedList[cellIndex].entropy <= leastEntropyCell.entropy:
                leastEntropyCell = unassignedList[cellIndex]
                leastEntropyCellIndex = cellIndex
        
        leastEntropyCell.selectRandom(smp.weights)
        assignedList.append(leastEntropyCell)
        del unassignedList[leastEntropyCellIndex]
        propagate(smp.weights, smp.neighbors, board, leastEntropyCell)

        if timeLapse:
            printBoard(board, M, N)
            time.sleep(.1)
            os.system("cls")

    idBoard = {c:board[c].tile for c in board}
    # 7.
    #im = Image.fromarray(np.uint8(myarray1)).convert('RGB')
    #im.save("kdkmdf.png")

    picsAsListsById = {}
    for imagePathId in smp.images:
        if imagePathId == 0: continue
        picsAsListsById[imagePathId] = np.array(Image.open(smp.images[imagePathId])).tolist()

    finalImage = []
    # TEM UMA FÓRMULA PARA O PIXEL FINAL, CERTEZA
    for i in range(M*16):
        line = []
        for j in range(N*16):
            line.append(picsAsListsById[idBoard[(i//16, j//16)]][i%16][j%16])
        finalImage.append(line)

    im = Image.fromarray(np.uint8(finalImage)).convert('RGB')
    im.save("save.png")

# if main
if __name__ == "__main__":
    main(34,22,False)