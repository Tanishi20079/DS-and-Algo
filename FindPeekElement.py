#peek element with O(logn) using binary search

arr=[1,2,1,3,5,6,8,7]
lo,hi=0,len(arr)-1
while lo<hi:
    m=lo+(hi-lo)//2
    if arr[m]>arr[m+1]:
        hi=m
    else:
        lo=m+1
print(arr[lo])
