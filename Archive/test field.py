from lib import Grid
import numpy as np


# ######################################
# # TEST 03:
grid = Grid()
print(grid)

# ######################################
# # TEST 03:
# grid = Grid(True)
# print(grid)
# grid = grid.shuffle()
# print(grid)
# print(grid.get_empty_coord())
# print('>> ', grid.grid[0][1])
# print(grid.org_pos(grid.grid[0][1]))


# ######################################
# # TEST 02:
# grid = Grid([6, 7, 1, 3, 2, 4, 0, 8, 5])
# grid2 = grid.copy()
# print(grid.grid)
# print(grid2)
# print(type(grid2))
# print(grid.solved())


# ######################################
# # TEST 01:
# custom = [[6, 7, 1], [3, 2, 4], [0, 8, 5]]
# custom = [6, 7, 1, 3, 2, 4, 0, 8, 5]
# # print(np.reshape(custom, (3, 3)))
# # print([j for sub in custom for j in sub])
# # print([[custom[3*i+j] for j in range(3)] for i in range(3)])

# grid = Grid(custom)
# print(grid.grid)

# ######################################
# TEST 01:
# perfect = Grid.get_perfect_grid()
# print(perfect)
