def longestincrseq(arr):
    l=[1]*len(arr)
    for i in range(1,len(arr)):
        for j in range(0,i):
            if arr[i]>arr[j] and l[i]<l[j]+1:
                l[i]=l[j]+1
    return max(l)
s=list(map(int,input().split()))
print(longestincrseq(s))





###########Second Method---->
A=[3, 10, 2, 1, 20]
d={}
count=0
for i in reversed(range(len(A))):
    s=A[i:]
    c=0
    for j in s:
        if j>A[i]:
            if j in d.keys():
                # print(d[j])
                c=max(c,d[j]+1)
            else:
                c+=1
    d[A[i]]=c
    count=max(c,count)
print(count+1)
    
