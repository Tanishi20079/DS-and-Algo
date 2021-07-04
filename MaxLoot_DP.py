#You are given a money present in n adjacent houses. There is a robber who wants to rob but can never rob in two adjacent houses. Find max amount he robs from houses.

n=4
arr=[6, 1, 3, 9]
dp=[-1]*(n+1)
def dpTopDown(arr,n):
    if n==0:
        return arr[0]
    if n==1:
        return max(arr[1],arr[0])
    dp[n]=max(arr[n]+dpTopDown(arr,n-2), dpTopDown(arr,n-1))
    return dp[n]

print(dpTopDown(arr,n-1))
