from tile import Tile

def returnSimpleSample(tileList : list[Tile]) -> tuple[list]:
    neighbors = {}
    weights = {}
    emojiMap = {}
    images = {}

    for tile in tileList:
        neighbors[tile.id] = tile.neightbors
        weights[tile.id] = tile.weight
        emojiMap[tile.id] = tile.emojiRepresentation
        images[tile.id] = tile.imagePath

    return (neighbors, weights, emojiMap, images)