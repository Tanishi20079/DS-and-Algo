def bfs(s,k):
    q=[]
    q.append(k)
    visited=[False]*(len(s)+1)
    visited[k]=True
    while len(q)>0:
        y=q.pop(0)
        print(y,end=" ")
        for i in s[y]:
            if visited[i]==False:
                visited[i]=True
                q.append(i)
            

n,m=map(int,input().split())
s=[[]]*(n+1)
for _ in range(m):
    s1,s2=map(int,input().split())
    s[s1].append(s2)
    s[s2].append(s1)
root=int(input())
bfs(s,root)


