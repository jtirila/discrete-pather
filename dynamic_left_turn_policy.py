from copy import deepcopy

# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

forward = [[-1, 0],  # go up
           [0, -1],  # go left
           [1, 0],  # go down
           [0, 1]]  # go right
forward_name = ['up', 'left', 'down', 'right']

forwards = list(zip(forward, forward_name))

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0]  # given in the form [row,col,direction]
# direction = 0: up
#             1: left
#             2: down
#             3: right

goal = [2, 0]  # given in the form [row,col]

cost = [2, 1, 20]  # cost has 3 values, corresponding to making
                  # a right turn, no turn, and a left turn

ACTION_TO_COST = {"R": 2, "L": 20, "#": 1}

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------


def _delta_vector(current_cell, candidate):
    return list(map(sum, zip(candidate[:2], map(lambda x: (-1) * x, current_cell[:2]))))


def _away_facing(current_cell, candidate):
   return list(map(lambda x: (-1) * x, forward[current_cell[2]])) == _delta_vector(current_cell, candidate)


def _action_straight(current_cell, candidate):
    action_to_reach_candidate = _delta_vector(current_cell, candidate)
    return action_to_reach_candidate == forward[current_cell[2]]


def _action_left(current_cell, candidate):
    index = (current_cell[2] + 1) % 4
    return forward[index] == _delta_vector(current_cell, candidate)


def _action_right(current_cell, candidate):
    index = (current_cell[2] - 1) % 4
    return forward[index] == _delta_vector(current_cell, candidate)


def _added_cost_and_action(current_cell, candidate, cost):
    if _action_straight(current_cell, candidate):
        return cost[1], "#"
    elif _action_right(current_cell, candidate):
        return cost[0], "R"
    elif _action_left(current_cell, candidate):
        return cost[2], "L"
    else:
        raise RuntimeError("Nooooope")


def _free_cell(candidate, grid):
    return candidate[0] in range(len(grid)) and candidate[1] in range(len(grid[0])) and \
           grid[candidate[0]][candidate[1]] == 0


def _sort_reachable_cells(reachable_cells):
    return list(sorted(reachable_cells, key=lambda x: x[3]))


def _orientation_index(delta_vector):
    return forward.index(delta_vector)


def _reachable_cells(current_cell, grid, cost):
    reachable_cells = []
    for forward, forward_name in forwards:
        # FIXME: fix orientation and cost
        candidate = list(map(sum, zip(current_cell[:4], forward + [0, 0]))) + [0]
        if not _away_facing(current_cell, candidate) and _free_cell(candidate, grid):
            candidate[2] = _orientation_index(_delta_vector(current_cell, candidate))
            cost_add, action = _added_cost_and_action(current_cell, candidate, cost)
            candidate[3] = current_cell[3] + cost_add
            candidate[4] = deepcopy(current_cell[4][:][:])
            candidate[4][current_cell[0]][current_cell[1]] = action
            reachable_cells.append(candidate)
    return reachable_cells


def _min_cost(reachable_cells):
    return min(map(lambda x: x[3], reachable_cells))


def optimum_policy2D(grid, init, goal, cost):
    action_list_template = [[' '] * len(grid[0]) for _ in grid]
    reachable_cells = [init + [0] + [deepcopy(action_list_template)]]
    goal_reaching_cells = []
    while True:
        reachable_cells = _sort_reachable_cells(reachable_cells)
        reachable_cells.reverse()
        new_current = reachable_cells.pop()
        reachable_cells.reverse()
        new_reachable_cells = _reachable_cells(new_current, grid, cost)
        reachable_cells += new_reachable_cells
        if not reachable_cells or (goal_reaching_cells and _min_cost(goal_reaching_cells) <= _min_cost(reachable_cells)):
            break
        for cell in new_reachable_cells:
            if cell[:2] == goal:
                cell[4][goal[0]][goal[1]] = "*"
                goal_reaching_cells.append(cell)
                index_of_cell = new_reachable_cells.index(cell)
                new_reachable_cells = new_reachable_cells[:index_of_cell] + new_reachable_cells[index_of_cell + 1:]

    goal_reaching_cells = list(sorted(goal_reaching_cells, key=lambda x: x[3], reverse=True))
    return goal_reaching_cells[0]


a = [0, 1, 0, 0]
b = [1, 1, 0, 0]
c = [0, 0, 0, 0]
d = [0, 2, 0, 0]
e = [1, 3, 0, 0]

cell = optimum_policy2D(grid, init, goal, cost)

for row in cell[4]:
    print(row)
