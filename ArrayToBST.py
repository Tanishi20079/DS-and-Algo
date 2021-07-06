#arry to bst
c=[]

def arrayToBST(l,r,s):
    if l<=r:
        y=(l+r)//2
        if c[y]:
            c[y]=False
            print(s[y],end=' ')
            arrayToBST(l,y-1,s)
            arrayToBST(y+1,r,s)


n=int(input())
s=list(map(int,input().split()))
c=[True]*n
c[(n-1)//2]=False
print(s[(n-1)//2],end=' ')
arrayToBST(0,(n-1)//2-1,s)
arrayToBST((n-1)//2+1,n-1,s)
print('')
