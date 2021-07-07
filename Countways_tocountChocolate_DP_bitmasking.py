#count ways to count chocolate dp bitmasking

# Input-
# 3
# 1 1 1
# 1 0 1 
# 1 1 1
#Output- 4


def countWays(like):
    n=len(like)
    dp=[0]*(1<<n)
    dp[len(dp)-1]=1
    for mask in range((1<<n)-2,-1,-1):
        k=str(bin(mask)).count('1')
        for i in range(n):
            if like[k][i] and (mask>>i)&1==0:
                dp[mask]+=dp[mask|(1<<i)]
    return dp[0]
        
n=int(input())
l=[]
for i in range(n):
    p=list(map(int,input().split()))
    l.append(p)
print(countWays(l))
