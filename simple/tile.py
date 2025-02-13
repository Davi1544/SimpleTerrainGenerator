class Tile:

    count = 0

    def __init__(self,
                 name : str = "",
                 weight : int = 0,
                 neighbors : list = [],
                 emojiRepresentation : str = "",
                 id : int = 0):
        
        self.id = id if id != 0 else Tile.count
        self.name = name
        self.weight = weight
        self.neightbors = neighbors
        self.emojiRepresentation = emojiRepresentation
        Tile.count += 1