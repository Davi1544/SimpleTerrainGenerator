import builder


sample2 = [
    ["1","pure water",2,{"N":{"w"},"E":{"w"},"S":{"w"},"W":{"w"}},"./SimpleTerrainGenerator/sockets/res/water.png","+"],
    ["2","sand",2,{"N":{"s"},"E":{"s"},"S":{"s"},"W":{"s"}},"./SimpleTerrainGenerator/sockets/res/sand.png","+"],
    ["3","corner sand",1,{"N":{"s"},"E":{"s"},"S":{"w"},"W":{"w"}},"./SimpleTerrainGenerator/sockets/res/cornerSand.png","!"],
    ["4","side sand",1,{"N":{"s"},"E":{"s"},"S":{"s"},"W":{"w"}},"./SimpleTerrainGenerator/sockets/res/sideSand.png","!"]
]

tiles = builder.build(sample2)