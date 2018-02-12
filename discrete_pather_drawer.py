# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
#
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left,
# up, and down motions. Note that the 'v' should be
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']
deltas = list(zip(delta, delta_name))


def search(grid, init, goal, cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------

    # JMT note: modified the code below, seemed off to me
    closed = [[0] * len(grid[0]) for _ in grid]
    closed[init[0]][init[1]] = 1

    expand_list = [[-1] * len(grid[0]) for _ in grid]
    cost_list = [[-1] * len(grid[0]) for _ in grid]
    draw_list = [[' '] * len(grid[0]) for _ in grid]

    x = init[1]
    y = init[0]
    g = 0

    open = [[g, y, x]]

    found = False  # flag that is set when search is complete
    resign = False  # flag set if we can't find expand
    expand_counter = 0

    while not found and not resign:
        if len(open) == 0:
            resign = True
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[2]
            y = next[1]
            g = next[0]

            expand_list[y][x] = expand_counter
            cost_list[y][x] = g

            expand_counter += 1

            if x == goal[1] and y == goal[0]:
                found = True
            else:
                for delta, delta_name in deltas:
                    x2 = x + delta[1]
                    y2 = y + delta[0]
                    if x2 in range(len(grid[0])) and y2 in range(len(grid)):
                        if closed[y2][x2] == 0 and grid[y2][x2] == 0:
                            g2 = g + cost
                            open.append([g2, y2, x2])
                            closed[y2][x2] = 1

    if resign:
        return False

    draw_list[goal[0]][goal[1]] = '*'
    pos = [goal[0], goal[1]]
    while True:
        if cost_list[pos[0]][pos[1]] == 0:
            break
        for delta, delta_name in deltas:
            opp_delta = _opposite_delta(delta)
            candidate_pos_y = pos[0] + opp_delta[0]
            candidate_pos_x = pos[1] + opp_delta[1]
            if candidate_pos_x in range(len(grid[0])) and candidate_pos_y in range(len(grid)) and\
                    cost_list[candidate_pos_y][candidate_pos_x] == cost_list[pos[0]][pos[1]] - 1:
                draw_list[pos[0] + opp_delta[0]][pos[1] + opp_delta[1]] = delta_name
                pos[0] = candidate_pos_y
                pos[1] = candidate_pos_x

    return draw_list


def _opposite_delta(delta):
    if delta[0] == 0:
        return [delta[0], delta[1] * (-1)]
    else:
        return [delta[0] * (-1), delta[1]]



draw_list = search(grid, init, goal, cost)
if draw_list:
    for row in draw_list:
        print(row)
