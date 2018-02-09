# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


def search(grid, init, goal, cost, delta):
    # Plan:
    # while not finished and some space is still available for inspection:
    #  - Starting from the least-cost point, expand all the possibilities and remove original

    state_list = [[0] + init]
    visited = [[0] + init]
    while _not_done(goal, state_list) and len(state_list) > 0:
        state_list.sort(key=lambda x: x[0])
        state_list = state_list[1:] + _proceed(state_list[0], state_list, visited, grid, delta, cost)
        if len(state_list) == 0:
            return False
        visited += [state_list[0]]

    # return path


def _proceed(state, state_list, visited, grid, delta, cost):
    new_state_list = []
    for step in delta:
        candidate_state = [state[0] + cost] + [sum(x) for x in zip(state[1:3], step)]
        if _position_legal(candidate_state, state_list, visited, grid):
            new_state_list.append(candidate_state)
    return new_state_list


def _not_done(goal, state_list):
    if goal in _state_list_to_position_list(state_list):
        print(next(state for state in state_list if state[1] == goal[0] and state[2] == goal[1]))
        return False
    return True


def _state_list_to_position_list(state_list):
    return list(map(lambda x: x[1:3], state_list))


def _position_legal(state, state_list, visited, grid):
    return _in_available_grid_cell(state, grid) and \
            state[1:3] not in _state_list_to_position_list(state_list) and\
            state[1:3] not in _state_list_to_position_list(visited)


def _in_available_grid_cell(state, grid):
    return min(state[1:3]) > -1 and  \
        state[1] < len(grid) and \
        state[2] < len(grid[0]) and\
        grid[state[1]][state[2]] == 0


def _nowhere_to_go(state_list):
    False  # TODO


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]

# grid = [[0, 1],
#         [0, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1,  0],  # go down
         [0,  1]]  # go right

delta_name = ['^', '<', 'v', '>']

print(search(grid, init, goal, cost, delta))
