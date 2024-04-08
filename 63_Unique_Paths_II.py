def uniquePathsWithObstacles(grid) -> int:
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows-1, -1, -1):
        for col in range(cols-1, -1, -1):
            if grid[row][col] == 1:
                grid[row][col] = 0
                continue
            
            if row == rows-1 and col == cols-1:
                grid[row][col] = 1
                continue
            if row == rows-1:
                bottom = 0
            else:
                bottom = grid[row+1][col]
            if col == cols-1:
                right = 0
            else:
                right = grid[row][col+1]    
            grid[row][col] = bottom + right
    return grid[0][0]
                  
                  

result = uniquePathsWithObstacles(grid=[[0,0,0],[0,1,0],[0,0,0]])
print(result)