def heapify(arr,i):
    left=2*i+1
    right=2*i+2
    
    if left >=len(arr) and right >=len(arr):
        return
    
    index=i
    
    if right<len(arr) and arr[i]>arr[right]:
        index=right
    
    if arr[index]>arr[left]:
        index=left
    
    if index!=i:
        arr[index],arr[i]=arr[i],arr[index]
    
    heapify(arr,index)
    
    
def buildheap(arr):
    for i in range(len(arr)//2,-1,-1):
        heapify(arr,i)
    
    

s=[5,3,21,4,1,5,7]
print(s)
buildheap(s)
print(s)
