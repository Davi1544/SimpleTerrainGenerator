########################
# 
# STEPS
#
# 1. Define the tiles, their respective ids and additional information
# 2. Define the rules for neightboring tiles for each tile
# 3. Define the weights for each neightboring tile for each tile
# 4. Make an MN list of cell objects with no tile
# 5. Make an empty MN list of cells that are filled
# 6. Fill the list of filled cells while emptying the list of unassigned cells
#   6.1. Choose a cell 
#       6.1.1. Choose a random cell (first iteration)
#       6.1.2. Choose the cell with the least entropy (other iterations)
#   6.2. Fill it using its "tileOptions" list
#   6.3. Move the cell to the assigned cell list
#   6.4. Propagate the necessary information to its neightboring cells
#   6.5. If necessary, propagate again and again until all cells have been updated
#       6.5.1. This can be done by keeping a list of cells that were affected by a propagation and then propagating on them
#   6.6. Rinse and repeat  
# 7. Convert the filled list into an M by N image