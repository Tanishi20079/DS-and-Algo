# Input- 2 4   (array size 2 and total stones is 5)
# array---> 2 3
# choose an element x from array and remove exactly x stones from pile
#find who will win "first" or "second"?



n,m=map(int,input().split())
l=list(map(int,input().split()))
dp=[0]*(m+1)
for i in range(m+1):
    for val in l:
        if val>i:continue
        if dp[i-val]==0:dp[i]=1

# print(dp)
print("First" if dp[m]==1 else "Second")
    
