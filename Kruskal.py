def find(x,parent):
    if parent[x]==x:
        return x
    else:
        return find(parent[x],parent)
    return 0
n,m=map(int,input().split())
s=[]
for _ in range(m) :
    x,y,w=map(int,input().split())
    s.append([x,y,w])
s=sorted(s,key=lambda x:x[2])
visited=[0]*(n+1);cost=0
rank=[0]*(n+1)
parent=[i for i in range(n+1)]
q=0;k=0
while q<n:
    i=s[k]
    x=find(i[0],parent)
    y=find(i[1],parent)
    if x!=y:
        visited[i[1]]=1
        if rank[x]<rank[y]:
            parent[x]=y
            rank[y]+=1
            k+=1
        elif rank[y]<rank[x]:
            parent[y]=x
            rank[x]+=1
            k+=1
        else:
            parent[y]=x
            rank[x]+=1
            k+=1
        cost+=i[2]
        q+=1
print(cost)
