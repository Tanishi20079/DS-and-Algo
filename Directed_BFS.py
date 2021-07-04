#bfs for directed graph 
#number of total vertices=4 and root is 2
#Input-
# 4 6  
# 0 1
# 0 2
# 1 2
# 2 0
# 2 3
# 3 3
# 2
# Output-2 0 3 1




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
s={}
for _ in range(m):
    s1,s2=map(int,input().split())
    if s1 not in s.keys():
        s[s1]=[s2]
    else:
        s[s1].append(s2)
    # s[s2].append(s1)
root=int(input())
# print(s)
bfs(s,root)
