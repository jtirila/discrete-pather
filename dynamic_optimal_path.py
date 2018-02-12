# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 0]]


grid2 =  [[0, 0, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0],
         [0, 0, 1, 1, 1, 0],
         [0, 0, 0, 0, 1, 0]]


goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

values = [[99] * len(grid[0]) for _ in grid]
values[goal[0]][goal[1]] = 0

actions = [[" "] * len(grid[0]) for _ in grid]
actions[goal[0]][goal[1]] = "*"

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


OPPOSITE_ACTION_NAMES = { "^": "v",
                          ">": "<",
                          "<": ">",
                          "v": "^"}

deltas = list(zip(delta, delta_name))


def _in_grid(cell, grid):
    return cell[0] in range(len(grid)) and \
            cell[1] in range(len(grid[0])) and \
            grid[cell[0]][cell[1]] == 0


def _unprocessed(neighbor, values):
    return values[neighbor[0]][neighbor[1]] == 99


def _get_neighbor(cell, delta):
    return list(map(sum, list(zip(cell, delta))))


def _opposite_action(action):
    return OPPOSITE_ACTION_NAMES[action]


def optimum_policy(grid, goal, cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------

    # make sure your function returns a grid of values as
    # demonstrated in the previous video.

    cells_to_expand = [goal]

    new_cells_to_expand = []
    while cells_to_expand:
        cell = cells_to_expand.pop()
        for delta, delta_name in deltas:
            neighbor = _get_neighbor(cell, delta)
            if _in_grid(neighbor, grid) and _unprocessed(neighbor, values):
                new_cells_to_expand.append(neighbor)
                values[neighbor[0]][neighbor[1]] = values[cell[0]][cell[1]] + cost
                actions[neighbor[0]][neighbor[1]] = _opposite_action(delta_name)
        if not cells_to_expand:
            cells_to_expand = new_cells_to_expand
            new_cells_to_expand = []

    return actions

actions = optimum_policy(grid, goal, cost)
for value_row in actions:
    print(value_row)

