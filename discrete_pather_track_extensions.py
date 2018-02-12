# A note by repository maintainer: most of this code was provided by Udacity, and I have just made some slight
# modifications

# -----------
# User Instructions:
#
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid
# you return has the value 0.
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
                        try:
                            if closed[y2][x2] == 0 and grid[y2][x2] == 0:
                                g2 = g + cost
                                open.append([g2, y2, x2])
                                closed[y2][x2] = 1
                        except IndexError:
                            print("Noooope")
                            pass

    if resign:
        return False
    return expand_list


expand_list = search(grid, init, goal, cost)
if expand_list:
    for row in expand_list:
        print(row)

