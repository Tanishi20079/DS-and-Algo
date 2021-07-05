#no. of ways to reach bottom right from top left with only right or down moves.
# "#" is the blocked way and "." is clear path
# input
#      7 5
#      ....#
#      .....
#      .##..
#      ....#
#      #.#..
#      ..##.
#      ..#..

# Output- 5





n,m=map(int,input().split())
l=[]
for i in range(n):
    # p=input()
    p=[i for i in input()]
    l.append(p)
dp=[[0]*(m)]*(n)
dp[n-1][m-1]=1
for i in range(n-1,-1, -1):
    for j in range(m-1,-1,-1):
        if i==n-1 and j==m-1:
            continue
        if l[i][j]=='#':
            dp[i][j]=0
        else:
            s1=0 if i==n-1 else dp[i+1][j]
            s2=0 if j==m-1 else dp[i][j+1]
            dp[i][j]=s1+s2
print(dp[0][0])
            
            
            
