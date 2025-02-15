import sample4 as sample
import numpy as np
from PIL import Image
from cell import Cell
from random import randint
from tile import Tile

# helper methods
def rotate90degClockwise(mat : list[list[int]]): 
    # source: https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/
    n = len(mat)

    # Initialize the result matrix with zeros
    res = [[0] * n for _ in range(n)]

    # Flip the matrix clockwise using nested loops
    for i in range(n):
        for j in range(n):
            res[j][n - i - 1] = mat[i][j]

    # Update the original matrix with the result
    for i in range(n):
        for j in range(n):
            mat[i][j] = res[i][j]

def rotateImage(image: list[list[int]], times : int) -> None:
    for i in range(times): 
        rotate90degClockwise(image)



def propagate(source : Cell, board : dict[tuple, Cell], tiles : dict[str, Tile], socketSet : set):
    i, j = source.position

    affectedCells = []
    ic = [                  # ic => instanceCalculations
        [i-1,j,"S","N"],    # top cell
        [i+1,j,"N","S"],    # bottom cell
        [i,j-1,"E","W"],    # left cell
        [i,j+1,"W","E"]
    ]

    for icInstance in ic:
        if (icInstance[0], icInstance[1]) in board:
            highlightedCell = board[(icInstance[0], icInstance[1])]
            if not(highlightedCell.tileId != "0") and source.fittingSockets[icInstance[3]] != socketSet: 
                highlightedCellDirectionSocket = highlightedCell.fittingSockets[icInstance[2]].copy()
                commonSockets = highlightedCellDirectionSocket & source.fittingSockets[icInstance[3]]
                if commonSockets != highlightedCellDirectionSocket:
                    affectedCells.append(highlightedCell)
                highlightedCell.fittingSockets[icInstance[2]] = commonSockets.copy()
                highlightedCell.calculatePossibleTileIds(tiles)
                highlightedCell.calculateFittingSockets(tiles)
                highlightedCell.calculateEntropy(tiles)

    for cell in affectedCells:
        propagate(cell, board, tiles, socketSet)

###############
# MAIN FUNCTION
###############

def main(M : int, N : int, tiles : dict[str, Tile], defaultTileId : str) -> None:

    cellBoard : dict[tuple, Cell] = {}
    unassingnedCells : list[Cell] = []
    socketSet : set[str] = set()
    allTileIds : set[str] = set()

    #########################
    # maping tiles to their respective images
    #########################
    picturesAsListsById : dict[str, list] = {}
    for tileId in tiles:
        tile = tiles[tileId]
        img = np.array(Image.open(tile.imagePath)).tolist()
        rotateImage(img, tile.rotations)
        picturesAsListsById[tileId] = img
        allTileIds.add(tileId)

        for cardinalDirection in tile.sockets:
            for socketType in tile.sockets[cardinalDirection]:
                socketSet.add(socketType)

    ##########################
    # setting up helper lists
    ##########################
    for i in range(M):
        for j in range(N):
            cell = Cell((i,j), 
                        "0", 
                        {
                            "N":socketSet.copy(),
                            "E":socketSet.copy(),
                            "S":socketSet.copy(),
                            "W":socketSet.copy()
                        })
            cell.entropy = 10 # arbitrary value
            cell.possibleTileIds = allTileIds.copy()
            unassingnedCells.append(cell)
            cellBoard[(i,j)] = cell
            
    ##########################
    # filling in the id matrix
    ##########################
    # filling in first cell
    randomIndex = randint(0, M*N-1)
    firstFilledCell = unassingnedCells[randomIndex]
    
    # removing the cell from the unassingedBunch
    del unassingnedCells[randomIndex]

    # assingning value
    firstFilledCell.selectRandom(tiles)

    # propagating information
    propagate(firstFilledCell, cellBoard, tiles, socketSet)

    # repeating on other cells
    while len(unassingnedCells) > 0:
        leastEntropyCell = unassingnedCells[0]
        leastEntropyCellId = 0
        for cellId in range(len(unassingnedCells)):
            if unassingnedCells[cellId].entropy < leastEntropyCell.entropy:
                leastEntropyCell = unassingnedCells[cellId]
                leastEntropyCellId = cellId
        
        leastEntropyCell.selectRandom(tiles)
        propagate(leastEntropyCell, cellBoard, tiles, socketSet)
        del unassingnedCells[leastEntropyCellId]

    ##########################
    # creating final image
    ##########################
    # getting id board
    idBoard = {}
    for i in cellBoard:
        if cellBoard[i].tileId in allTileIds:
            idBoard[i] = cellBoard[i].tileId
        else: 
            idBoard[i] = defaultTileId

    # creating the final image
    finalImage = []
    for i in range(M*16):
        line = []
        for j in range(N*16):
            line.append(picturesAsListsById[idBoard[(i//16, j//16)]][i%16][j%16])
        finalImage.append(line)

    im = Image.fromarray(np.uint8(finalImage)).convert('RGB')
    im.save("saveSockets.png")

# if main
if __name__ == "__main__":
    main(100,100,sample.tiles,"1")