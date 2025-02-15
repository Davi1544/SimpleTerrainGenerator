from tile import Tile

def build(preBuildTiles : list) -> list[Tile]:
    tiles : dict[str, Tile] = {}
    for preTile in preBuildTiles:
        rotationStr : str = preTile[5]

        if rotationStr == "+":
            tiles[preTile[0]] = Tile(*preTile[0:5])

        elif rotationStr == "?":
            tiles[preTile[0]] = Tile(*preTile[0:5])

            # separating parameters
            id = preTile[0]
            name = preTile[1]
            weight = preTile[2]
            sockets = preTile[3]
            path = preTile[4]
            rotations = 0

            socketsE = {"N":sockets["S"],"E":sockets["W"],"S":sockets["N"],"W":sockets["E"]}
            rotations += 2
            rotations = rotations % 4
            name += "i"
            id += "i"

            tiles[id] = Tile(id,name,weight,socketsE,path,rotations)

        elif rotationStr == "-":
            tiles[preTile[0]] = Tile(*preTile[0:5])

            # separating parameters
            id = preTile[0]
            name = preTile[1]
            weight = preTile[2]
            sockets = preTile[3]
            path = preTile[4]
            rotations = 0

            socketsE = {"N":sockets["W"],"E":sockets["N"],"S":sockets["E"],"W":sockets["S"]}
            rotations += 1
            rotations = rotations % 4
            name += "i"
            id += "i"

            tiles[id] = Tile(id,name,weight,socketsE,path,rotations)

        elif rotationStr == "!":
            tiles[preTile[0]] = Tile(*preTile[0:5])

            # separating parameters
            id = preTile[0]
            name = preTile[1]
            weight = preTile[2]
            sockets = preTile[3]
            path = preTile[4]
            rotations = 0

            for rotationIdLetter in ["i","j","k"]:
                rotationName = name + rotationIdLetter
                rotationId = id + rotationIdLetter
                sockets = {"N":sockets["W"],"E":sockets["N"],"S":sockets["E"],"W":sockets["S"]}
                rotations += 1
                rotations = rotations % 4

                tiles[rotationId] = Tile(rotationId,rotationName,weight,sockets,path,rotations)

    return tiles
