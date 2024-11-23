import heapq

class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex src.
    def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
        # Your code here
        
        priority_queue=[]
        heapq.heappush(priority_queue,(0,src))
        
        cost=[10**9]*len(adj)
        cost[src]=0
        
        while len(priority_queue)>0:
            dist,node=priority_queue.pop(0)
            for i in adj[node]:
                d=dist+i[1]
                if cost[i[0]]>d:
                    cost[i[0]]=d
                    heapq.heappush(priority_queue,(cost[i[0]],i[0]))
            # break
    
        # print(priority_queue, cost)
        return cost
