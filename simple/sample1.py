import builder
from tile import *

tilesInfo = [
    Tile("",0,{0},""),
    Tile("Tall grass",1,{1,2},"\U0001F33E","./SimpleTerrainGenerator/simple/res/tallGrass.png"),        # Tall Grass
    Tile("Grass",3,{1,2,3,4,6},"\U0001F33F","./SimpleTerrainGenerator/simple/res/grass.png"),           # Grass
    Tile("Path",1,{2,3,4},"\U0001F7EB","./SimpleTerrainGenerator/simple/res/path.png"),              # Path
    Tile("House",1,{2,3,4},"\U0001F3E0","./SimpleTerrainGenerator/simple/res/house.png"),               # House
    Tile("Water",2,{5,6},"\U0001F7E6","./SimpleTerrainGenerator/simple/res/water.png"),                # Water
    Tile("Sand",2,{5,6,2},"\U0001F7E8","./SimpleTerrainGenerator/simple/res/sand.png"),
]
# emoji_map = {
#     0: " ",
#     5: "\U0001F7E6",  # Water 
#     6: "\U0001F7E8",  # Sand 
#     1: "\U0001F33E",  # Tall Grass 
#     2: "\U0001F33F",  # Grass 
#     3: "\U0001F7EB",  # Path 
#     4: "\U0001F3E0",  # House 
#     7: "\U0001F30A",  # Wave
#     8: "\U0001F3E1",   # House with Garden
#     9: "\U0001F3E2"   # Office Building
# }
# tiles = [
#         "",
#         "tall grass",  
#         "grass",
#         "path",
#         "house",
#         "water",
#         "sand",
#         "wave",
#         "House with garden",
#         "Office Building"
#     ]

# neighbors = {
#         0 : {0},
#         1 : {1,2},
#         2 : {1,2,3,4,6,8},
#         3 : {2,3,4,9},
#         4 : {2,3,4},
#         5 : {5,6,7},
#         6 : {5,6,2},
#         7 : {5},
#         8 : {2},
#         9 : {4,3}
#     }


# weights = {
#         0 : 0,
#         1 : 1,
#         2 : 3,
#         3 : 2,
#         4 : 1,
#         5 : 3,
#         6 : 2,
#         7 : 1,
#         8 : 1,
#         9 : 1
#     }


neighbors, weights, emojiMap, images = builder.returnSimpleSample(tilesInfo)