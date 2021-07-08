#find-three-closest-elements-from-given-three-sorted-arrays
def threeclosest(a1,a2,a3,p,q,r):
    diff=10**9+7
    i,j,k=0,0,0
    posi,posj,posk=0,0,0
    while i<p and j<q and k<r:
        mini=min(a1[i],a2[j],a3[k])
        maxi=max(a1[i],a2[j],a3[k])
        if maxi-mini<diff:
            posi,posj, posk=i,j,k
            diff=maxi-mini
        if diff==0:
            break
        if a1[i]==mini:
            i+=1
        elif a2[j]==mini:
            j+=1
        else:
            k+=1
    print(a1[posi]," ",a2[posj]," ",a3[posk])


A = [1, 4, 10]
B = [2, 15, 20]
C = [10, 12]
 
p = len(A)
q = len(B)
r = len(C)
threeclosest(A,B,C,p,q,r)
            
        
