# LCS with O(nm)
def lcs(x,y,m,n):
    l=[[None]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                l[i][j]=0
            elif x[i-1]==y[j-1]:
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i][j-1],l[i-1][j])
    return l[m][n]
x,y=input(),input()
print(lcs(x,y,len(x),len(y)))
                
