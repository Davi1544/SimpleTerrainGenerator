import builder


sample3 = [
    ["1","empty",150,{"N":{"nada"},"E":{"nada"},"S":{"nada"},"W":{"nada"}},"./SimpleTerrainGenerator/sockets/res/empty.png","+"],
    ["2","straight rail",70,{"N":{"trilho"},"E":{"nada"},"S":{"trilho"},"W":{"nada"}},"./SimpleTerrainGenerator/sockets/res/straightRail.png","-"],
    ["3","corner rail",5,{"N":{"trilho"},"E":{"trilho"},"S":{"nada"},"W":{"nada"}},"./SimpleTerrainGenerator/sockets/res/cornerRail.png","!"],
    ["4","corner minecart",1,{"N":{"trilho"},"E":{"trilho"},"S":{"nada"},"W":{"nada"}},"./SimpleTerrainGenerator/sockets/res/cornerMinecart.png","!"],
    ["5","gems",1,{"N":{"nada"},"E":{"nada"},"S":{"nada"},"W":{"nada"}},"./SimpleTerrainGenerator/sockets/res/gems.png","+"],
    ["6","rail end",1,{"N":{"nada"},"E":{"trilho"},"S":{"nada"},"W":{"nada"}},"./SimpleTerrainGenerator/sockets/res/railEnd.png","!"],
    ["7","pedra",1,{"N":{"nada"},"E":{"pedra"},"S":{"nada"},"W":{"pedra"}},"./SimpleTerrainGenerator/sockets/res/straightWall.png","-"],
    ["8","pedra stop",5,{"N":{"nada"},"E":{"nada"},"S":{"nada"},"W":{"pedra"}},"./SimpleTerrainGenerator/sockets/res/wallStop.png","!"],
    ["9","pedra joint 3",5,{"N":{"pedra"},"E":{"pedra"},"S":{"nada"},"W":{"pedra"}},"./SimpleTerrainGenerator/sockets/res/wallJoint3.png","!"],
    ["10","pedra joint 4",100,{"N":{"pedra"},"E":{"pedra"},"S":{"pedra"},"W":{"pedra"}},"./SimpleTerrainGenerator/sockets/res/wallJoint4.png","+"],
    ["11","pedra corner",2,{"N":{"nada"},"E":{"pedra"},"S":{"pedra"},"W":{"nada"}},"./SimpleTerrainGenerator/sockets/res/stoneCorner.png","!"]
]

tiles = builder.build(sample3)