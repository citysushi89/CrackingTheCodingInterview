"""
breadth_first_search.py contains a func bfs which performs a binary search
can be used with graph.py
"""


# Simple bfs
def bfs(graph, source):
    visited = [False] * len(graph.data)
    queue = []
    
    visited[source] = True    
    queue.append(source)
    i = 0
    
    while i < len(queue):
        for v in graph.data[queue[i]]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
        i += 1
        
    return queue


# bfs with weights, distances, parents
def bfs_w_weights(graph, root):
    queue = []
    discovered = [False] * len(graph.data)
    distance = [None] * len(graph.data)
    parent = [None] * len(graph.data)
    
    discovered[root] = True
    queue.append(root)
    distance[root] = 0
    idx = 0
    
    while idx < len(queue):
        # Dequeue operation
        current = queue[idx]
        idx += 1
        
        for node in graph.data[current]:
            if not discovered[node]:
                distance[node] = 1 + distance[current]
                parent[node] = current
                discovered[node] = True
                queue.append(node)
                
    return queue, distance, parent
        