# Count no. of ways to cover a distance n using 1, 2 and 3 steps
################################################################
# method 1: O(3^n)
def countways(n):
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return (countways(n-1)+countways(n-2)+countways(n-3))
n=int(input())
print(countways(n))
#################################################################
#method 2:O(n)
def countways(n):
    count=[0]*(n+1)
    count[0]=1
    count[1]=1
    count[2]=2
    for i in range(3,n+1):
        count[i]=count[i-1]+count[i-2]+count[i-3]
    return count[n]
print(countways(int(input())))
