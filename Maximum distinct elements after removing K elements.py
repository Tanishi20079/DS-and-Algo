n,k=map(int,input().split())
s=list(map(int,input().split()))
d=dict()
count=0
no_use=0
for i in s:
    if i in d:
        no_use+=1
        d[i]+=1
    else:
        d[i]=1
        count+=1
print(d)
if k<=no_use:
    print(count)
else:
    print(count-(k-no_use))
