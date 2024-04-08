import sys


def uniquePaths(m, n) -> int:
    grid = [[0 for x in range(n)] for y in range(m)]
    paths = 0
    maximum = sys.maxsize
    for row in range(m - 1, -1, -1):
        for col in range(n - 1, -1, -1):
            if row == m - 1 and col == n - 1:
                grid[row][col] = 1
                continue
            if row == m - 1:
                below = 0
            else:
                below = grid[row + 1][col]
            if col == n - 1:
                right = 0
            else:
                right = grid[row][col + 1]

            grid[row][col] = below + right
    return grid[0][0]


result = uniquePaths(m=3, n=2)
print(result)
