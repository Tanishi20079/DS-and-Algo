#max heap

heap=[]
def upheapify(heap,idx):
    if idx==0:return 
    pi=(idx-1)//2
    if heap[pi]<heap[idx]:
        heap[idx],heap[pi]=heap[pi],heap[idx]
        upheapify(heap, pi)
    else:
        return 
    
    
def downheapify(heap,i):
    li,ri=2*i+1,2*i+2
    if li>=len(heap) and ri>=len(heap):return
    max_idx=i
    if li<len(heap) and heap[li]>heap[max_idx]:max_idx=li
    if ri<len(heap) and heap[ri]>heap[max_idx]:max_idx=ri
    if max_idx==i:return
    heap[i],heap[max_idx]=heap[max_idx],heap[i]
    downheapify(heap,max_idx)
    
def deletePeek(heap):
    heap[0],heap[len(heap)-1]=heap[len(heap)-1],heap[0]
    heap.pop()
    downheapify(heap,0)

def delete_at_x(heap,x):
    heap[x]=10**9
    downheapify(heap,0)
    deletePeek(heap)
    
    

n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    heap.append(l[i])
    upheapify(heap,i)
print(heap)
deletePeek(heap)
x=int(input("Enter element for deleting"))
delete_at_x(heap,heap.index(x))
print(heap)
