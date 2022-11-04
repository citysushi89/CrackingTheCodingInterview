"""
A robot is sitting in the upper left corner of a grid with r rows and c columns
robot can only move in 2 directions, right and down but certain cells are 'off limits'
design an algorithm to find a path for the robot from the top left to the bottom right
NOTE: robot currently tries to go right first, until encountering edge of the grid or
an off limits square, then it goes down
"""

GRID_SIZE = (4, 4)
ROBOT_LOCATION = (0, 0)

class Grid:
    grid_layout = []
    def __init__(self, grid_size, off_limits_grids=None) -> None:
        self.grid_size = grid_size
        if off_limits_grids is None:
            self.off_limits_grids = []
        else:
            self.off_limits_grids = off_limits_grids

        for r in range(grid_size[0]):
            row_list = []
            for c in range(grid_size[1]):
                row_list.append((r, c))
            self.grid_layout.append(row_list)

    def get_possible_moves(self, location):
        possible_moves = []
        possible_move_d = (location[0] + 1, location[1])
        if possible_move_d not in self.off_limits_grids and possible_move_d[0] <= self.grid_size[0]:
            possible_moves.append(possible_move_d)
        possible_move_r = (location[0], location[1] + 1)
        if possible_move_r not in self.off_limits_grids and possible_move_r[1] <= self.grid_size[1]:
            possible_moves.append(possible_move_r)
        return possible_moves


def move_right(location, possible_moves):
    row = location[0] 
    col = location[1] + 1
    new_location = (row, col)
    if new_location in possible_moves:
        return new_location
    else:
        return -1

def move_down(location, possible_moves):
    row = location[0] + 1
    col = location[1]
    new_location = (row, col)
    if new_location in possible_moves:
        return new_location
    else:
        return -1


grid = Grid(GRID_SIZE, off_limits_grids=[(0, 1)])


old_location = ROBOT_LOCATION
while True:
    moves = grid.get_possible_moves(old_location)
    if moves:
        for potential_move in moves:
            if old_location[1] + 1 == potential_move[1]:
                new_location = move_right(old_location, moves)
            elif old_location[0] + 1 == potential_move[0]:
                new_location = move_down(old_location, moves)

        old_location = new_location
        if new_location not in grid.off_limits_grids:
            continue

    if new_location == grid.grid_size:
        print('found bottom right corner')
        break



