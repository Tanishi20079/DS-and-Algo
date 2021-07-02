def isSafe(grid, n, i, j):
    #column check
    for row in reversed(range(0,i)):
        if grid[row][j]:
            return False
            
    #left upper diagonal
    col=j-1
    for row in reversed(range(0,i)):
        if col>=0 and grid[row][col]:
            return False
        col-=1
        
    #right upper diagonal
    col=j+1
    for row in reversed(range(0,i)):
        if col<n and grid[row][col]:
            return False
        col+=1
    return True
    
            
def countNQueen(grid, cur_row, n, count):
    if cur_row==n:
        # print(count+1)
        return count+1
    for i in range(n):
        if isSafe(grid, n, cur_row, i):
            grid[cur_row][i]=True
            count=countNQueen(grid, cur_row+1, n, count)
            grid[cur_row][i]=False
    return count
            
n=5
grid=[[False for i in range(n)] for j in range(n)]

print(countNQueen(grid, 0, n,0))

    
    
    
