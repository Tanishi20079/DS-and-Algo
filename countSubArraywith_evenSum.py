#number of sub arrays having even sum
n=int(input())
s=list(map(int,input().split()))
count=0
l=[]
for i in range(n):
    t=s[i]
    if t%2==0:
        count+=1
    for j in range(i+1,n):
        t+=s[j]
        if t%2==0: 
            count+=1
print(count)
