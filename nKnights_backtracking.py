ans=0
def isSafe(r, c, grid, n):
    if r-2>=0 and c-1>=0 and grid[r-2][c-1]:return False
    if r-1>=0 and c-2>=0 and grid[r-1][c-2]:return False
    if r-2>=0 and c+1<n and grid[r-2][c+1]:return False
    if r-1>=0 and c+2<n and grid[r-1][c+2]:return False
    return True

def nKnights(n, grid, cur_row, col, count):
    global ans
    if count==n:
        ans+=1
        # display(grid,n)
        return 
    
    for i in range(cur_row,n):
        p=col if i==cur_row else 0
        for j in range(p,n):
            if isSafe(i,j,grid,n):
                grid[i][j]=True
                nKnights(n,grid,i, j+1,count+1)
                grid[i][j]=False

# def display(grid,n):
#     for i in range(n):
#         for j in range(n):
#             print(grid[i][j],end=" ")
#         print("\n")
#     print("\n",end="\n")

n=3
grid=[[False for i in range(n)] for j in range(n)]
nKnights(n,grid, 0, 0, 0)
print(ans)
            
        
    
    
    
    

    
