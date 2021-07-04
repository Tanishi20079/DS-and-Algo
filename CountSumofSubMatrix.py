#count sum of all possible sub matrices of a given matrix.
#example---> matrix=[[1,2],[1,3]]   subset are- {[1],[2],[1],[3],[1,2],[1,3],[1,1] #column-wise,[2,3] #column-wise,[1,2,1,3]} therefore sum=28

def countSumofSubMatrix(arr):
    n=len(arr)
    m=len(arr[0])
    s=0
    for i in range(n):
        for j in range(m):
            cur_topleft=(i+1)*(j+1)
            cur_bottomright=(n-i)*(m-j)
            s+=arr[i][j]*(cur_bottomright*cur_topleft)
    return s

s=[[1,2],[2,3]]
print(countSumofSubMatrix(s))
