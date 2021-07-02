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
        display(grid,n)
        return count+1
    for i in range(n):
        if isSafe(grid, n, cur_row, i):
            grid[cur_row][i]=True
            count=countNQueen(grid, cur_row+1, n, count)
            grid[cur_row][i]=False
    
    return count
    
    
def display(grid, n):
    for i in range(n):
        s=''
        for j in range(n):
            if grid[i][j]:
                s+="Q"
            else:
                s+="."
        print(s)
                
    
            
n=5
grid=[[False for i in range(n)] for j in range(n)]
count=countNQueen(grid, 0, n,0)
# print(grid)
print(count)
# display(grid, n)


    
    
    
