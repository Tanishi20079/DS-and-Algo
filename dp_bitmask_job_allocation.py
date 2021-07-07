# dp with bitmask job allocation
#given N*N array having n jobs and n workers
# Input-->
# 4
# 3 2 7 4
# 5 6 1 2
# 5 3 1 5
# 4 6 11 3
#Output---> 9



def count_bits(mask):
    count=0
    while mask>0:
        count+=1
        mask=mask&(mask-1)
    return count

def minCost(cost):
    n=len(cost)
    dp=[10**9+7]*(1<<n)
    dp[0]=0
    for i in range(1<<n):
        worker=count_bits(i)
        for j in range(n):
            if i>>j & 1 ==1:
                continue
            else:
                dp[i|(1<<j)]=min(dp[i|(1<<j)],dp[i]+cost[worker][j])
    return dp[(1<<n)-1]
    
n=int(input())
arr=[]
for i in range(n):
    p=list(map(int,input().split()))
    arr.append(p)
print(minCost(arr))
    
            
