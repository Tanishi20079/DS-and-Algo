def dfs(s,ss,visited):
    print(ss,end=' ')
    for i in s[ss]:
        if visited[i]==False:
            visited[i]=True
            dfs(s,i,visited)
n,m=map(int,input().split())
s=[[] for i in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    s[x].append(y)
    s[y].append(x)
k=int(input())
visited=[False]*(n+1)
visited[k]=True
dfs(s,k,visited)
