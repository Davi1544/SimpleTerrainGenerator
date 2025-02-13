from tile import Tile

def returnSimpleSample(tileList : list[Tile]) -> tuple[list]:
    neighbors = {}
    weights = {}
    emojiMap = {}

    for tile in tileList:
        neighbors[tile.id] = tile.neightbors
        weights[tile.id] = tile.weight
        emojiMap[tile.id] = tile.emojiRepresentation

    return (neighbors, weights, emojiMap)