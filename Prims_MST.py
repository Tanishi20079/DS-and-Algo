import heapq

def primsMinimumSpanningTree(graph):
    queue = [(0, '#', list(graph.keys())[0])]
    tree = []
    seen = set()
    while queue:
        _, v0, v1 = heapq.heappop(queue)
        seen.add(v0)
        if v1 not in seen:
            tree.append((v0,v1))
            for (v2, c) in graph[v1].items():
                heapq.heappush(queue, (c, v1, v2))
    return tree
			
graph = {
	'a': {'w': 14, 'x': 7, 'y': 9},
    'b': {'w': 9, 'z': 6},
    'w': {'a': 14, 'b': 9, 'y': 2},
    'x': {'a': 7, 'y': 10, 'z': 15},
    'y': {'a': 9, 'w': 2, 'x': 10, 'z': 11},
    'z': {'b': 6, 'x': 15, 'y': 11},
} 
print(primsMinimumSpanningTree(graph))
