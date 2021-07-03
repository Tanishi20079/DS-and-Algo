#space complexity O(n) instead of O(n*n)

ans=0
def nqueen(n, cr):
    global ans
    if cr==n:
        ans+=1
        return 
    for c in range(n):
        if col[c]==0 and ld[cr-c+n-1]==0 and rd[cr+c]==0:
            col[c]=ld[cr-c+n-1]=rd[cr+c]=1
            nqueen(n, cr+1)
            col[c]=ld[cr-c+n-1]=rd[cr+c]=0

    
n=6
col=[0 for i in range(100)]
ld=[0 for i in range(100)]
rd=[0 for i in range(100)]
nqueen(n,0)
print(ans)
            
            
        
    
    
    
    

    
