import builder


sample4 = [
    ["1","empty shelf",50,{"N":{"sh"},"E":{"nd"},"S":{"sh"},"W":{"nd"}},"./SimpleTerrainGenerator/sockets/res/sample4/emptyShelf.png","+"],
    ["2","close",1,{"N":{"sh"},"E":{"nd"},"S":{"sh"},"W":{"sh"}},"./SimpleTerrainGenerator/sockets/res/sample4/leftClose.png","!"],
    ["3","one side",20,{"N":{"air"},"E":{"air"},"S":{"sh"},"W":{"air"}},"./SimpleTerrainGenerator/sockets/res/sample4/bottomShelf.png","?"],
    ["4","full",20,{"N":{"sh"},"E":{"psh"},"S":{"sh"},"W":{"psh"}},"./SimpleTerrainGenerator/sockets/res/sample4/pureShelf.png","+"],
    ["5","joint3",1,{"N":{"psh"},"E":{"psh"},"S":{"sh"},"W":{"psh"}},"./SimpleTerrainGenerator/sockets/res/sample4/pureShelfJoint3.png","!"],
    ["6","3books",50,{"N":{"sh"},"E":{"nd"},"S":{"sh"},"W":{"nd"}},"./SimpleTerrainGenerator/sockets/res/sample4/books.png","+"],
    ["7","fullbooks",50,{"N":{"sh"},"E":{"nd"},"S":{"sh"},"W":{"nd"}},"./SimpleTerrainGenerator/sockets/res/sample4/fullBooks.png","+"],
    ["8","flower",10,{"N":{"sh"},"E":{"nd"},"S":{"sh"},"W":{"nd"}},"./SimpleTerrainGenerator/sockets/res/sample4/flower.png","+"],
    ["9","hanging flower",2,{"N":{"sh"},"E":{"air"},"S":{"air"},"W":{"air"}},"./SimpleTerrainGenerator/sockets/res/sample4/hanging.png","+"],
    ["10","last books",20,{"N":{"sh"},"E":{"nd"},"S":{"sh"},"W":{"nd"}},"./SimpleTerrainGenerator/sockets/res/sample4/lastBooks.png","+"]

]

tiles = builder.build(sample4)