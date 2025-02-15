import builder

# ROTATION CODES :
# +     =>      no extra rotation tiles
# -     =>      add rotation by 90deg tile
# !     =>      add rotations by every 90 deg rotation

preBuildTiles = [
    ["1","empty",1,{"N":{"e"},"E":{"e"},"S":{"e"},"W":{"e"}},"./SimpleTerrainGenerator/sockets/res/empty.png","+"],
    ["2","straight",2,{"N":{"e"},"E":{"t"},"S":{"e"},"W":{"t"}},"./SimpleTerrainGenerator/sockets/res/straight.png","-"],
    ["3","curve",2,{"N":{"t"},"E":{"t"},"S":{"e"},"W":{"e"}},"./SimpleTerrainGenerator/sockets/res/curve.png","!"],
    ["4","flower",2,{"N":{"e"},"E":{"e"},"S":{"t"},"W":{"e"}},"./SimpleTerrainGenerator/sockets/res/flower.png","!"],
    ["5","split",2,{"N":{"t"},"E":{"t"},"S":{"e"},"W":{"t"}},"./SimpleTerrainGenerator/sockets/res/split.png","!"],
    ["6","joint",2,{"N":{"t"},"E":{"t"},"S":{"t"},"W":{"t"}},"./SimpleTerrainGenerator/sockets/res/joint.png","+"],
    ["7","rose",2,{"N":{"e"},"E":{"e"},"S":{"r"},"W":{"e"}},"./SimpleTerrainGenerator/sockets/res/rose.png","!"],
    ["8","redStraight",2,{"N":{"r"},"E":{"e"},"S":{"r"},"W":{"e"}},"./SimpleTerrainGenerator/sockets/res/redStraight.png","-"],
    ["8","mixedJoint",2,{"N":{"r"},"E":{"t"},"S":{"r"},"W":{"t"}},"./SimpleTerrainGenerator/sockets/res/mixedJoint.png","-"]  
]



tiles = builder.build(preBuildTiles)