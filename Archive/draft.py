import numpy as np
from random import randint
from time import time

# #################################################################
# def solution(node):
#     visited = set()
#     queue = set()
#     queue.add(node)
#     visited.add(node.state)

#     while queue:
#         node_childs2 = list()
#         node = min(queue, key= lambda x: x.state)
#         queue.remove(node)
#         if node.solved:
#             return node.path

#         node_childs = node.get_childs()
#         for child in node_childs:
#             if child.state not in visited:
#                 queue.add(child)
#                 visited.add(child.state)
#                 node_childs2.append(child)
#     return node.path
# #################################################################

# def get_grids_childs(self):
#     grids = []
#     moving_blocks = self.grid.moving_blocks()

#     for action, block in moving_blocks.items():
#         copy = deepcopy(self.grid)

#         copy.make_move(action, block)
#         grids.append(copy)
#     return grids


# #################################################################
# def random_move(self):
#     copy = self.copy()
#     block_can_move = copy.moving_blocks()
#     rand_block = choice(list(block_can_move.items()))[1]
#     copy = copy.make_move(rand_block)
# #################################################################
# if mouse_coord in state.moving_blocks.items():
#     print('>> IT CAN MOVE!')
#     # make_move(action, to)
# if can_move_to(grid, mouse_position, empty_pos):
#     print('>> IT CAN MOVE!')
#     make_transition(grid, mouse_position, empty_pos)

# #################################################################
#
#
# def solution(node):
#     # doka node lowel diro fell file then fell while :
#     # lwhile dir while not solved:
#     # sort file
#     # edi least cost element
#     # diro visited
#     open_Nodes = deque([node])
#     visited = set()
# visited.add(node.state)
# # print(node)

# while not node.solved:

#     node = open_Nodes.popleft()
#     node_childs = node.get_childs()
#     #
#     nodes_print(node, node_childs)
#     #
#     for child in node_childs:
#         if child.state not in visited:
#             visited.add(node.state)
#             open_Nodes.appendleft(child)
#     open_Nodes = deque(
#         sorted(list(open_Nodes), key=lambda node: node.score))
# return node.path

#
# #################################################################


# def is_solvable(puzzle):
#     em = 0
#     # A utility function to count
#     # inversions in given array 'arr[]'

#     def getInvCount(arr):
#         arr[arr.index(em)] = -1
#         inv_count = 0
#         empty_value = -1
#         for i in range(0, 9):
#             for j in range(i + 1, 9):
#                 if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
#                     inv_count += 1
#         return inv_count
#     # Count inversions in given 8 puzzle
#     inv_count = getInvCount([j for sub in puzzle for j in sub])
#     # return true if inversion count is even.
#     return (inv_count % 2 == 0)
# #################################################################

# def nodes_print(node, node_childs):
#     if len(node_childs) == 4:
#         print('{:<12} - {:<13} - {:<13} - {:<13} - {:<13}'.format('Grid:',
#                                                                   'Move_1 ' +
#                                                                   str(node_childs[0].action_char) + '/' +
#                                                                   str(node_childs[0].h),
#                                                                   'Move_2 ' +
#                                                                   str(node_childs[1].action_char) + '/' +
#                                                                   str(node_childs[1].h),
#                                                                   'Move_3 ' +
#                                                                   str(node_childs[2].action_char) + '/' +
#                                                                   str(node_childs[2].h),
#                                                                   'Move_4 ' +
#                                                                   str(node_childs[3].action_char) + '/' +
#                                                                   str(node_childs[3].h)))
#         for i in range(3):
#             print('{:<12} - {:<13} - {:<13} - {:<13} - {:<13}'.format(str(node.grid.grid[i]),
#                                                                       str(
#                 node_childs[0].grid.grid[i]),
#                 str(
#                 node_childs[1].grid.grid[i]),
#                 str(
#                 node_childs[2].grid.grid[i]),
#                 str(node_childs[3].grid.grid[i])))
#     if len(node_childs) == 3:
#         print('{:<12} - {:<13} - {:<13} - {:<13}'.format('Grid:',
#                                                          'Move_1 ' +
#                                                          str(node_childs[0].action_char) + '/' +
#                                                          str(node_childs[0].h),
#                                                          'Move_2 ' +
#                                                          str(node_childs[1].action_char) + '/' +
#                                                          str(node_childs[1].h),
#                                                          'Move_3 ' +
#                                                          str(node_childs[2].action_char) + '/' +
#                                                          str(node_childs[2].h)))
#         for i in range(3):
#             print('{:<12} - {:<13} - {:<13} - {:<13}'.format(str(node.grid.grid[i]),
#                                                              str(node_childs[0].grid.grid[i]),
#                                                              str(node_childs[1].grid.grid[i]),
#                                                              str(node_childs[2].grid.grid[i])))
#     if len(node_childs) == 2:
#         print('{:<12} - {:<13} - {:<13}'.format('Grid:',
#                                                 'Move_1 ' +
#                                                 str(node_childs[0].action_char) + '/' +
#                                                 str(node_childs[0].h),
#                                                 'Move_2 ' +
#                                                 str(node_childs[1].action_char) + '/' +
#                                                 str(node_childs[1].h)))
#         for i in range(3):
#             print('{:<12} - {:<13} - {:<13}'.format(str(node.grid.grid[i]),
#                                                     str(node_childs[0].grid.grid[i]),
#                                                     str(node_childs[1].grid.grid[i])))
#     if len(node_childs) == 1:
#         print('{:<12} - {:<13}'.format('Grid:',
#                                        'Move_1 ' +
#                                        str(node_childs[0].action_char) + '/' +
#                                        str(node_childs[0].h)))
#         for i in range(3):
#             print('{:<12} - {:<13}'.format(str(node.grid.grid[i]),
#                                            str(node_childs[0].grid.grid[i])))

# #################################################################
# TP2 v2


# def can_move_to(grid, current_pos, next_pos):
#     if grid[next_pos[0]][next_pos[1]] or current_pos == next_pos:
#         return False
#     line, col = next_pos
#     return any([
#         bool(0 <= line-1 < 3 and (line-1, col) == current_pos),
#         bool(0 <= line+1 < 3 and (line+1, col) == current_pos),
#         bool(0 <= col-1 < 3 and (line, col-1) == current_pos),
#         bool(0 <= col+1 < 3 and (line, col+1) == current_pos)
#     ])


# def is_solvable(puzzle):
#     # A utility function to count
#     # inversions in given array 'arr[]'
#     def getInvCount(arr):
#         arr[arr.index(Grid.em)] = -1
#         inv_count = 0
#         empty_value = -1
#         for i in range(0, 9):
#             for j in range(i + 1, 9):
#                 if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
#                     inv_count += 1
#         return inv_count
#     # Count inversions in given 8 puzzle
#     inv_count = getInvCount([j for sub in puzzle for j in sub])
#     # return true if inversion count is even.
#     return (inv_count % 2 == 0)


# def get_get_perfect_grid(kernal=3):
#     # center = kernal//2
#     # perf_grid = list(range(1, kernal**2))
#     # perf_grid.append(em)
#     # grid = np.reshape(perf_grid, (kernal, kernal))
#     # grid[-1][-1], grid[center][center] = grid[center][center], em
#     return np.array([[1, 2, 3],
#                      [4, Grid.em, 5],
#                      [6, 7, 8]])
#     # return np.reshape([i for i in range(1, 10)], (3, 3)).tolist()


# def get_random_grid(kernal=3):
#     center = kernal//2
#     numbers, grid = list(range(1, kernal**2)), []
#     while numbers:
#         grid.append(numbers.pop(randint(0, len(numbers)-1)))
#     grid.append(Grid.em)
#     grid = np.reshape(grid, (kernal, kernal))

#     grid[-1][-1], grid[center][center] = grid[center][center], Grid.em
#     return grid


# def get_grid(kernal=3, random=True, custom=False):
#     if custom:
#         return np.reshape(custom, (3, 3))
#     #
#     # if random:
#     #     for _ in range(100):
#     #         make_random_transition(grid)
#     #
#     grid = get_get_perfect_grid(kernal)
#     if random:
#         solvable = False
#         while not solvable:
#             for _ in range(300):
#                 make_random_transition(grid)
#             solvable = is_solvable(grid)
#             if not solvable:
#                 print(grid)
#                 grid = get_get_perfect_grid(kernal)
#     #
#         print(grid)
#         print('>>', is_solvable(grid))
#     return grid


# def pos_avail(grid, pos):
#     return bool(grid[pos[0]][pos[1]])
#     # return not grid[pos[0]][pos[1]]


# def empty_square_coord(grid):
#     empty = np.where(grid == Grid.em)
#     return (empty[0][0], empty[1][0])


# def block_that_can_move(grid):
#     # or we can call it possible transition
#     empty = empty_square_coord(grid)
#     block_that_can_move = {}
#     poss_moves = {
#         'RIGHT': (empty[0], empty[1]+1),
#         'LEFT_': (empty[0], empty[1]-1),
#         'DOWN_': (empty[0]+1, empty[1]),
#         'UP___': (empty[0]-1, empty[1])
#     }
#     for direc, (line, col) in poss_moves.items():
#         if 0 <= line < 3 and 0 <= col < 3:
#             block_that_can_move[direc] = (line, col)
#     return block_that_can_move


# def can_move_to(grid, current_pos, next_pos):
#     if grid[next_pos[0]][next_pos[1]] or current_pos == next_pos:
#         return False
#     line, col = next_pos
#     return any([
#         bool(0 <= line-1 < 3 and (line-1, col) == current_pos),
#         bool(0 <= line+1 < 3 and (line+1, col) == current_pos),
#         bool(0 <= col-1 < 3 and (line, col-1) == current_pos),
#         bool(0 <= col+1 < 3 and (line, col+1) == current_pos)
#     ])
#     # return any([
#     #     bool(0 <= line-1 < 3 and [line-1, col] == next_pos),
#     #     bool(0 <= line+1 < 3 and [line+1, col] == next_pos),
#     #     bool(0 <= col-1 < 3 and [line, col-1] == next_pos),
#     #     bool(0 <= col+1 < 3 and [line, col+1] == next_pos)
#     # ])


# def move_to(grid, old, new):
#     grid[new[0]][new[1]], grid[old[0]][old[1]
#                                        ] = grid[old[0]][old[1]], grid[new[0]][new[1]]
#     # grid[old[0]][old[1]] = em


# def make_transition(grid, pos, dest):
#     if can_move_to(grid, pos, dest):
#         move_to(grid, pos, dest)
#         return True
#     return False


# def make_random_transition(grid):
#     block_can_move = block_that_can_move(grid)
#     rand_block = choice(list(block_can_move.items()))[1]
#     move_to(grid, rand_block, empty_square_coord(grid))


# def is_solvable(puzzle):
#     em = 0
#     # A utility function to count
#     # inversions in given array 'arr[]'

#     def getInvCount(arr):
#         arr[arr.index(em)] = -1
#         inv_count = 0
#         empty_value = -1
#         for i in range(0, 9):
#             for j in range(i + 1, 9):
#                 if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
#                     inv_count += 1
#         return inv_count
#     # Count inversions in given 8 puzzle
#     inv_count = getInvCount([j for sub in puzzle for j in sub])
#     # return true if inversion count is even.
#     return (inv_count % 2 == 0)


#################################################################
# def prepare_grid(instance):
#     # isinstance(l, np.ndarray)
#     if isinstance(instance, str):
#         if len(instance) == 9:
#             return np.array(list(instance), dtype=np.uint8).reshape(3, 3)
#         else:
#             raise Exception("There should be 9 Numbers (form 0 to 8)..!!!")
#     elif isinstance(instance, list) or isinstance(instance, np.ndarray) or isinstance(instance, tuple):
#         if len(instance) == 9:
#             return np.array(instance, dtype=np.uint8).reshape(3, 3)
#         else:
#             return np.array(instance, dtype=np.uint8)
#             # raise Exception("There should be 9 Numbers (form 0 to 8)..!!!")
#             # TO-DO : less code if i test if len()==9 first...
#     else:
#         raise Exception(
#             "Unsupported Type ,only <str, list, tuple or np.ndarray>")

def prepare_grid(instance):
    if len(instance) == 3:
        for item in instance:
            if len(item) > 3:
                raise Exception(
                    "Length should be 9 or 3x3 (in a range of 0 to 8)..!!!")
    elif len(instance) != 9:
        raise Exception(
            "There should be 9 Numbers (in a range of 0 to 8)..!!!")

    instance = np.array(list(instance), dtype=np.uint8).reshape(3, 3)
    for val in np.nditer(instance):
        if not 48 <= ord(str(val)) <= 56:
            raise Exception(
                "Unsupported Val/val_Type ,only numbers from 0 To 8 !")
    return instance


t1 = time()
t = prepare_grid([1, 2, 3, 4, 5, 6, 7, 8, 0])
print(time()-t1)
print(t)
print(type(t))

# [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
#################################################################
