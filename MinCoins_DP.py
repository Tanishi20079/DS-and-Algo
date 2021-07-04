#coins=[1,5,7] sum=11
#1+5+5=11 or 1+1+1+1+....1(11 times)=11 or 1+1+1+1+7=11 so the minimum coins required to make sum 11 is 3


def mincoins(n,s,dp,coins):
    if s<0:return 10**9+7
    if s==0:return 0
    if dp[s]!=-1:return dp[s]
    result=10**9+7
    for i in range(n):
        recursionResult=mincoins(n,s-coins[i],dp,coins)
        if recursionResult==10**9+7:
            continue
        result=min(result,1+recursionResult)
    dp[s]=result
    return dp[s]


coins=[1,5,7]
n=11
dp=[-1]*(n+1)
print(mincoins(len(coins),n,dp,coins))
        
