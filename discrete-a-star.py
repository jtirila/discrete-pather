# -----------
# User Instructions:
#
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
#
# If there is no path from init to goal,
# the function should return the string 'fail'
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']
deltas = list(zip(delta, delta_name))

# JMT note: another thing I don't like about the template's coding style:
# some of the data structures defined above are provided into the search
# functions as parameters whereas others (delta...) are just used as globals.


def search(grid, init, goal, cost, heuristic):
    # ----------------------------------------
    # modify the code below
    # ----------------------------------------
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1

    # JMT note: I would prefer a not-so-low-level implementation of many parts of the
    # implementation stub provided by Udacity. Below an example of something that could
    # be rewriteen in a more Pythonic way.
    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    action = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False  # flag set if we can't find expand
    count = 0

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return "Fail"
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[2]
            y = next[1]
            g = next[0]
            expand[y][x] = count
            count += 1

            if x == goal[1] and y == goal[0]:
                found = True
            else:
                for delta, delta_name in deltas:
                    x2 = x + delta[1]
                    y2 = y + delta[0]
                    if x2 in range(len(grid[0])) and y2 in range(len(grid)):
                        if closed[y2][x2] == 0 and grid[y2][x2] == 0:
                            g2 = g + cost + heuristic[y2][x2] - heuristic[y][x]
                            if x == y == 0:
                                g2 += heuristic[y][x]
                            open.append([g2, y2, x2])
                            action[y2][x2] = delta_name
                            closed[y2][x2] = 1

    return expand


expanded = search(grid, init, goal, cost, heuristic)
for line in expanded:
    print(line)
