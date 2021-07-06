n=int(input())
s=list(map(int,input().split()))
i=0;j=n-1;count=0;s.sort()
while i<j:
    count+=(s[i]*s[j])
    i+=1;j-=1
print(count)
