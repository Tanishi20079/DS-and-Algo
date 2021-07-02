#Given N*N bound with the knight placed at (0,0). check if the knight can cover all the cells of the board, using its usual chess moves without visiting any cell twice

def isSafe(grid, n, i, j, visited):
    return i>=0 and j>=0 and i<n and j<n and visited[i][j]==False
    
            
def knightTours(grid, n, i, j, count,visited):
    if count==n*n-1:
        grid[i][j]=count
        display(grid, n)
        return 
    if count>=n*n:
        return
    xdir=[-2,-2,-1,-1,2,2,1,1]
    ydir=[1,-1,2,-2,1,-1,2,-2]
    visited[i][j]=True
    grid[i][j]=count
    for k in range(8):
        if isSafe(grid,n, i+xdir[k],j+ydir[k],visited):
           knightTours(grid,n,i+xdir[k],j+ydir[k],count+1,visited)
    grid[i][j]-=1
    visited[i][j]=False

        
    
def display(grid, n):
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=" ")
        print()
    print("\n")
                
    
            
n=5
grid=[[-1 for i in range(n)] for j in range(n)]
visited=[[False for i in range(n)] for j in range(n)]
knightTours(grid, n, 0, 0,0,visited)
# display(grid, n)
