import numpy as np
from time import time
from copy import deepcopy
from random import choice
from collections import deque

"""
    game_lib library, contain the classes and methods that we need
    to relaise the game.
    """
# #################################################################
# Game settings :
"""
    boolean parameters, to pause the game, indicate the end of the game, quitting game (resp).
    indicates the computer turn, waiting time(we pass it to pyGame interface), and the color we used.
    """
pause, game_over, quit_game = False, False, False
computer_turn = True
waiting_time = 500
colors = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yahoo': (144, 14, 158),
    'tumblr': (54, 70, 93)
}

# #################################################################


class Grid:
    """
    This class represent a grid of 3 by 3 (8-puzzle).
    grid should b an 3x3 matrix of numbers(0 to 8), e.g: [[6, 5, 2], [4, 3, 1], [0, 8, 7]]
        you can use prepare_grid() to get a grid that is ready to use(check its doc).

    Raises:
        "Length should be 9 or 3x3 (in a range of 0 to 8)..!!!": in case of the list that we passed to prepare_grid() method
                                                                    isn't a list of 9 items, or a matrix of 3 col, 3 rows.
        "There should be 9 Numbers (in a range of 0 to 8)..!!!": in case of the list that we passed to prepare_grid() method
                                                                    isn't a list of 9 item.
        "Unsupported Val/val_Type ,only numbers from 0 To 8 !": in case of the list that we passed to prepare_grid() method
                                                                    contain numbers or strings other then the numbers from 0 to 8.
    """
    x, y = 'x', 'y'
    em = 0
    Grid_used = 0
    # class attribute are shared acroos all instance of class
    perfect_grid = np.array([[1, 2, 3], [4, em, 5], [6, 7, 8]])

    @classmethod
    def get_perfect_grid(cls):
        """
        classmethod that return a perfect grid.
        e.g [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
        """
        grid = Grid(custom=np.array([[1, 2, 3], [4, Grid.em, 5], [6, 7, 8]]))
        return grid

    @classmethod
    def get_random_grid(cls):
        """
        classmethod that return a random grid(by shuffling a perfect grid many times).
        e.g [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
        """
        grid = Grid.get_perfect_grid()
        grid = grid.shuffle()
        return grid

    @classmethod
    def prepare_grid(cls, instance):
        """
        classmethod that prepare and make sure that this grid can be used. 
        you can pass a list of 9 numbers(0 to 8) or a normal matrix.
        PS: call it only when you need it, do not put it into the __init__ method
        to avoid slowing down the program(will be called unnecessarily each time we creat a class)
        
        Args:
            instance (list): list of 9 numbers or a matrix of 3 by 3.

        Returns:
            instance: matrix of 3x3 numbers(from 0 to 8).
        """
        if len(instance) == 3:
            for item in instance:
                if len(item) > 3:
                    # raising an Exception in case of there more then 3 numbers in each line
                    raise Exception(
                        "Length should be 9 or 3x3 (in a range of 0 to 8)..!!!")
        elif len(instance) != 9:
                # raising an Exception in case there is more or les then 8 numbers.
            raise Exception(
                "There should be 9 Numbers (in a range of 0 to 8)..!!!")
        # reshaping the list into a matrix of 3x3.
        instance = np.array(list(instance), dtype=np.uint8).reshape(3, 3)
        for val in np.nditer(instance):
            # chr(48) == '0' and chr(56) == '8'
            if not 48 <= ord(str(val)) <= 56:
                # raising an Exception in case there is a number that isn't equal or in between 8 and 0
                # or a string
                raise Exception(
                    "Unsupported Val/val_Type ,only numbers from 0 To 8 !")
        return instance

    def __init__(self, custom=None):
        self.grid = np.array(custom)
        Grid.Grid_used += 1

    @property
    def manhattan(self):
        # grid = np.delete(np.reshape(grid, 9), np.where(grid == em))
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.grid[i][j]:
                    #
                    x, y = np.where(Grid.perfect_grid ==
                                    self.grid[i][j])  # [:][:2]
                    x, y = x[0], y[0]
                    #
                    distance += abs(x-i) + abs(y-j)
        return distance

    @property
    def empty_coord(self):
        return (np.where(self.grid == Grid.em)[0][0], np.where(self.grid == Grid.em)[1][0])

    def moving_blocks(self):
        empty = self.empty_coord
        block_can_move = {}
        poss_moves = {
            'RIGHT': (empty[0], empty[1]+1),
            'LEFT_': (empty[0], empty[1]-1),
            'DOWN_': (empty[0]+1, empty[1]),
            'UP___': (empty[0]-1, empty[1])
        }
        for direc, (line, col) in poss_moves.items():
            if 0 <= line < 3 and 0 <= col < 3:
                block_can_move[direc] = (line, col)
        return block_can_move

    def make_move(self, action, to):
        copy = self.copy()
        y_empty, x_empty = copy.empty_coord
        copy.grid[y_empty][x_empty] = copy.grid[to[0]][to[1]]
        copy.grid[to[0]][to[1]] = 0
        return copy, action

    def can_move(self, to):
        y, x = to
        return self.empty_coord in (
            (y, x-1),
            (y, x+1),
            (y-1, x),
            (y+1, x)
        )

    def make_action(self, action):
        y_empty, x_empty = self.empty_coord
        moves = {
            'R': (y_empty, x_empty+1),
            'L': (y_empty, x_empty-1),
            'D': (y_empty+1, x_empty),
            'U': (y_empty-1, x_empty)
        }
        return self.make_move(action, moves[action])[0]

    def shuffle(self, moves_range=380):
        puzzle = self
        for _ in range(moves_range):
            block_can_move = puzzle.moving_blocks()
            puzzle = puzzle.make_move(
                *choice(tuple(block_can_move.items())))[0]
            # puzzle = self.make_move(*choice(tuple(block_can_move.items())))[0]
        return puzzle

    @property
    def solved(self):
        return str(self) == '123405678'

    def copy(self):
        Grid.Grid_used += 1
        return deepcopy(self)

    def __str__(self):
        # EXP: '314205867'
        return ''.join(list(map(str, [j for sub in self.grid for j in sub])))

    def __eq__(self, other):
        return str(self) == str(other)

# #################################################################


class Node:

    def __init__(self, grid, parent=None, action=None):
        self.grid = grid
        self.parent = parent
        self.action = action
        if (self.parent == None):
            self.g = 0
        else:
            self.g = parent.g + 1

    def get_childs(self):
        nodes = []
        moving_blocks = self.grid.moving_blocks()
        for action, block in moving_blocks.items():
            temp_node = Node(self.grid.copy().make_move(
                action, block)[0], self, action)
            nodes.append(temp_node)
        return nodes

    @property
    def action_char(self):
        return self.action[0]

    @property
    def path(self):
        path = ''
        node = self
        while node.action != None:
            path += node.action_char
            node = node.parent
        return path[::-1]

    @property
    def score(self):
        return self.g + self.h

    @property
    def h(self):
        return self.grid.manhattan

    @property
    def solved(self):
        return self.grid.solved

    @property
    def state(self):
        # EXP: '314205867'
        return str(self.grid)

    def __str__(self):
        return str(self.grid)+str(self.action)+str(self.parent)

# #################################################################


def solution(node):
    """_summary_

    Args:
        node (_type_): _description_

    Returns:
        _type_: _description_
    """
    visited = set()
    queue = deque([node])
    visited.add(queue[0].state)

    while queue:
        queue = deque(sorted(list(queue), key=lambda node: node.score))
        node = queue.popleft()
        if node.solved:
            return node.path

        # TODO: yeild childs instead of getting them all
        node_childs = node.get_childs()
        for child in node_childs:
            if child.state not in visited:
                queue.appendleft(child)
                visited.add(child.state)
    return node.path


# #################################################################
# TEST :
if __name__ == '__main__':
    # custom_list = [[1, 2, 3], [0, 5, 7], [6, 4, 8]]
    # custom_list = [[3, 2, 0], [7, 1, 4], [8, 6, 5]]
    # custom_list = [[1, 6, 8], [4, 0, 2], [7, 5, 3]]  # 387735
    # initial_grid = Grid(Grid.prepare_grid(custom_list))

    initial_grid = Grid.get_random_grid()
    node = Node(initial_grid)

    start_time = time()
    path = solution(node)

    print(initial_grid)
    print('>> path:', path)
    print('>> ', len(path))
    print('>> Grid used:', Grid.Grid_used)
    print(f'>> TIME: {time()-start_time} Second(s)')
