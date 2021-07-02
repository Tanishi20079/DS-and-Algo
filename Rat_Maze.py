def issafe(i, j, n,m, visited):
    # print(i>=0 and j>=0 and i<n and j<m and not visited[i][j])
    return i>=0 and j>=0 and i<n and j<m and not visited[i][j]
    
def helper(i, j ,n, m, maze, visited,count):
    if i==n-1 and j==m-1:
        count+=1
        return count
    if not issafe(i, j , n, m, visited):
        return count
    visited[i][j]=True
    # print("hello")
    if i+1<n and maze[i+1][j]==0:
        count=helper(i+1, j, n, m , maze, visited, count)
    if i-1>=0 and maze[i-1][j]==0:
        count=helper(i-1, j, n, m , maze, visited, count)
    if j+1<m and maze[i][j+1]==0:
        count=helper(i, j+1, n, m , maze, visited, count)
    if j-1>=0 and maze[i][j-1]==0:
        count=helper(i, j-1, n, m , maze, visited, count)
    visited[i][j]=False
    return count
  

def countPaths(maze, n, count):
    visited=[[False for j in range(n) ] for i in range(n)]
    # print(visited)
    count=helper(0,0,n, n, maze, visited, count)
    return count
    
    
count=0
maze = []
n=int(input())
for i in range(n):
    l=list(map(int,input().split()))
    maze.append(l)
print(countPaths(maze, n,0))
