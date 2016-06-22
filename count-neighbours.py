dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [-1, 1, -1, 0, 1, -1, 0, 1]

def in_bounds(low, high, n):
    return low <= n and n < high

def count_neighbours(grid, row, col):
    neighbours = 0
    columns = len(grid[0])
    rows = len(grid)

    for i in range(len(dx)):
        if in_bounds(0, rows, row + dx[i]) and\
           in_bounds(0, columns, col + dy[i]):
            neighbours += grid[row + dx[i]][col + dy[i]]
    return neighbours
