def recurse(arr,word,n,i,r,c):
    if i>=len(word):return False
    if r<0 or r>=n or c<0 or c>=n:return False
    if arr[r][c]!=word[i]:return False
    arr[r][c]='$'
    retval=False
    row=[-1,1,0,0]
    col=[0,0,-1,1]
    for j in range(len(row)):
        retval=recurse(arr,word,n,i+1,r+row[j],c+col[j])
        if retval:
            break
    arr[r][c]=word[i]
    return retval
        


def find(arr,word,n):
    for i in range(n):
        for j in range(n):
            if arr[i][j]==word[0]:
                if(recurse(arr,word,n,0,i,j)):
                    return True
    return False


grid=[['A','B'],['C','D']]
word="ACF"
print(find(grid,word,len(grid)))
