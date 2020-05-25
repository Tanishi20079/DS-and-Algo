def longestincrseq(arr):
    l=[1]*len(arr)
    for i in range(1,len(arr)):
        for j in range(0,i):
            if arr[i]>arr[j] and l[i]<l[j]+1:
                l[i]=l[j]+1
    return max(l)
s=list(map(int,input().split()))
print(longestincrseq(s))
