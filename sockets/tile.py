class Tile:

    count = 0

    def __init__(self,
                 id : str = "0",
                 name : str = "",
                 weight : int = 0,
                 sockets : dict[str, set[str]] = [], # N, E, S, W
                 imagePath : str = "",
                 rotationsBy90degCounterClock : int = 0, # how many image rotations are necessary?
                ): 
        
        Tile.count += 1
        self.id = id if id != "0" else str(Tile.count)
        self.name = name
        self.weight = weight
        self.sockets = sockets
        self.imagePath = imagePath
        self.rotations = rotationsBy90degCounterClock


    def __str__(self):
        return f"Tile named {self.name} with id {self.id} and weight {self.weight}. The sockets are {self.sockets}. {self.rotations} (clockwise) 90deg image rotations are necessary to represent this tile"