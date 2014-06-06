#!/bin/python

# Maze solver

from itertools import permutations

SPACE = " "
WALL = "#"
PATH = "*"
START = "S"
EXIT = "E"
STACK = []

test_maze = """\
#########################################
#   #       #     #           #         #
# # # ### # # ### # ####### ### ####### #
# #S#   # #   #   # #     #           # #
# ##### # ######### # # ############# # #
# #     # #         # #       #   #   # #
# # ##### # ######### ##### # # # # ### #
# #     #   #     #     #   # # # # # # #
# ##### ######### # ##### ### # # # # # #
#   #           #   #     #   # # #   # #
# ### ######### # ### ##### ### # ##### #
#   #   #     # # #   #       # #       #
# # ### # ### # ### ### ####### ####### #
# #     # #   #     #   # #     #     # #
# ####### # ########### # # ##### # ### #
#     # # #   #       #   # #   # #     #
##### # ##### # ##### ### # ### # #######
#   # #     # #   #   #   # #   #     # #
# ### ### ### ### # ### ### # ####### # #
#   #     #   #   # #   #   # #     #   #
### ##### # ### ### ### # ### # ### ### #
#       # #   # # #   # # #   # # #     #
# ####### ### # # ### ### # ### # #######
#       #   #   #   # #   #     #       #
# ##### ### ##### # # # ##### ### ### ###
#   # # #   #     # # #     # #     #   #
### # # # ### # ##### # ### # # ####### #
# #   #   #   # #     #   # # # #     # #
# ### ##### ### # ##### ### # # # ### # #
#   #       #   # # #   #   # # #   #   #
# # ######### ### # # ### ### # ### #####
# #     #   # # # #   #   # # #   #     #
# ##### # # # # # ### # ### # ######### #
# #   # # # # # #   # #   #             #
# # # # # # # # ### ### # ############# #
# # #     # # #   #   # #       #       #
# ######### # # # ### ### ##### # #######
#     #     # # #   #   # #     # #     #
# ### ####### ### # ### ### ##### # ### #
#   #             #   #     #       #E  #
#########################################"""

def construct_maze(string_repr: str):
    maze = []
    for line in string_repr.splitlines():
        maze.append([])
        for letter in line:
            maze[-1].append(letter)
    return maze

def find(character: str, maze: list) -> tuple:
    for index, row in enumerate(maze):
        if character in row:
            return (row.index(character), index)


def look_around(x: int, y: int, maze: list) -> list:
    open_spaces = []
    # Up, right, down, left // North, East, South, West
    cardinal_directions = (list(permutations((0,1), 2))
                           + list(permutations((0, -1), 2)))
    for x_offset, y_offset in cardinal_directions:
        new_x, new_y = x + x_offset, y + y_offset
        open_spaces.append(maze[new_y][new_x])
        print("{},{}:".format(new_x, new_y),maze[new_y][new_x])
    return open_spaces

def find_open_spaces(view: list) -> list:
    return [item for item in view if item == SPACE]

def can_see_end(view: list) -> bool:
    return "E" in view

def make_choice(x: int, y: int, maze: list) -> tuple:
    index_to_movement = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
    spaces = look_around(x, y, maze)
    # Lay down a breadcrumb
    maze[y][x] = PATH
    moves = find_open_spaces(spaces)
    # Reorganize moves: Right -> Left -> Up -> Down
    spaces = spaces[1::2] + spaces[::2]
    if can_see_end(spaces):
        print("Found the end!")
        for line in maze:
            print(''.join(line))
        return(0,0)
        #return("Found the end")
    # No more places to go
    if not moves:
        old_x, old_y = STACK.pop(-1)
        return make_choice(old_x, old_y, maze)
    # There is more than one way to go
    elif len(moves) > 1:
        STACK.append((x, y))
    decision = spaces.index(SPACE)
    # 0 is up, 1 is right, etc...
    new_x, new_y = index_to_movement.get(decision)
    x += new_x
    y += new_y
    return (x, y)

def loop(start_point: tuple, maze: list):
    x, y = start_point

    while True:
        x, y = make_choice(x, y, maze)
        if not x and not y:
            print("End point found!")
            break
        print("New Position: {}, {}".format(x, y))

maze_list = construct_maze(test_maze)
start_point = find(START, maze_list)
print("Start point: {}".format(start_point))
spaces = look_around(7, 6, maze_list)
print(spaces)
print(make_choice(7, 6, maze_list))
for index, i in enumerate(test_maze.splitlines()):
    print(index, i, sep='\t')
print(STACK)
loop(start_point, maze_list)
