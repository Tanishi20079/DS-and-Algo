#Input-
# 6 5
# 1 2
# 2 4
# 2 3
# 3 4
# 1 3
# 1
# Output-3


def dfsHelper(s,src, visited):
    visited[src]=True
    for neighbor in s[src]:
        if not visited[neighbor]:
            dfsHelper(s, neighbor, visited)
        

def connectedcomponents(s,root,n):
    component=0
    visited=[False]*(n+1)
    for i in range(1,n+1):
        if not visited[i]:
            component+=1
            dfsHelper(s,i,visited)
    return component

n,m=map(int,input().split())
s=[[]]*(n+1)
for i in range(m):
    s1,s2=map(int,input().split())
    s[s1].append(s2)
    s[s2].append(s1)
            
root=int(input())
print(connectedcomponents(s,root,n))

