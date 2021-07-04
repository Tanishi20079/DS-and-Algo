# done in O(nlogn+n+m) time


#Input-
# 2
# 4 1
# 1 3 2 4
# 1 4 2 3
# 3 4
# 4 1
# 1 3 2 4
# 1 4 2 3
# 2 4

# Output- 
# no 
# yes




def dfsHelper(s,src, visited, p, q, a, b):
    a.append(p[src])
    b.append(q[src])
    visited[src]=True
    for neighbor in s[src]:
        if not visited[neighbor]:
            dfsHelper(s, neighbor, visited, p, q, a, b)
    return a,b
            
            
test=int(input())
while test:
    n,m=map(int,input().split())
    p=list(map(int,input().split()))
    q=list(map(int,input().split()))
    s=[[]]*(n+1)
    while m:
        s1,s2=map(int,input().split())
        s[s1-1].append(s2-1)
        s[s2-1].append(s1-1)
        m-=1
    visited=[False]*n
    flag=True
    for i in range(n):
        if not visited[i]:
            a=[]
            b=[]
            a, b=dfsHelper(s, i, visited, p, q, a,b)
            a.sort()
            b.sort()
            if a!=b:
                flag=False
    if flag==False:
        print("no")
    else:print("yes")
    test-=1
            
    
        
    
    
