"""
breadth_first_search.py contains a func bfs which performs a binary search
can be used with graph.py
"""

def bfs(graph, root):
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
        