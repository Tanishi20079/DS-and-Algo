n=int(input())
s=list(map(int,input().split()))
i=0
while 2**i-1<n:
    i+=1
print(i-1)
