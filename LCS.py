# Lcs program with O(2^n) time complexity.
def lcs(x,y,n,m):
    if m==0 or n==0:
        return 0
    elif x[n-1]==y[m-1]:
        return 1+lcs(x,y,n-1,m-1)
    else:
        return max(lcs(x,y,n-1,m),lcs(x,y,n,m-1))
x,y=input(),input()
print(lcs(x,y,len(x),len(y)))
