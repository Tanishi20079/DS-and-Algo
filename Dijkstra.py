#Dijkstra Shortest Path


import heapq
def shortestPath(graph, start, end):
    queue,seen = [(0, start, [])], set()
    while True:
        (cost, v, path) = heapq.heappop(queue)
        if v not in seen:
            path = path + [v]
            seen.add(v)
            if v == end:
                return cost, path
            for (next, c) in graph[v].items():
                heapq.heappush(queue, (cost + c, next, path))
			
graph = { 
   'a': {'w': 14, 'x': 7, 'y': 9}, 
   'b': {'w': 9, 'z': 6}, 
   'w': {'a': 14, 'b': 9, 'y': 2}, 
   'x': {'a': 7, 'y': 10, 'z': 15}, 
   'y': {'a': 9, 'w': 2, 'x': 10, 'z': 11}, 
   'z': {'b': 6, 'x': 15, 'y': 11}, 
}
cost, path = shortestPath(graph, 'a', 'b')
print(cost, path)
