def subsetBacktrack(arr, n, i, l):
    if i==n:
        if len(l)>0:
            print(l)
        return
    l.append(arr[i])
    subsetBacktrack(arr, n, i+1, l)
    l.pop()
    subsetBacktrack(arr, n,i+1, l)

subsetBacktrack([1,2,3,4,5], 5, 0, [])
