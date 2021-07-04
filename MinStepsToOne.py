#Input n=10
#Output 3
# Explanation:-
# 10--->5--->4--->2--->1 steps=4
# 10--->9--->3--->1 stesp=3
#return min(3,4)

def minSteptoOne(n,dp):
    if n==2 or n==3:return 1
    if n==1:return 0
    if n<1: return 10**9+7
    if dp[n]!=0:
        return dp[n]
    div_by_3, div_by_2, sub_by_1=10**9+7,10**9+7,10**9+7
    if n%3==0:
        div_by_3=1+minSteptoOne(n//3,dp)
    if n%2==0:
        div_by_2=1+minSteptoOne(n//2,dp)
    sub_by_1=1+minSteptoOne(n-1,dp)
    dp[n]=min(div_by_2,div_by_3,sub_by_1)
    return dp[n]

n=14   
dp=[0]*(n+1)
print(minSteptoOne(n,dp))
    
