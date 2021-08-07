from heapq import heappush, heappop

def makeHeap(iterable):
    heap = [] 
    
    for value in iterable:
        heappush(heap, value)
    
    return heap

        
numbers = [
   15,25,1,8,7,16,21,2,4,13,6,5,12,22,34,14,18,28,24,20,17
]

# create a heap
heap = makeHeap(numbers)

# use as a priority queue:
result = []
while heap:
    result.append(heappop(heap))
print(result)
