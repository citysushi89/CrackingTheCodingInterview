"""
Given a list of projects and dependencies, find a build order that will allow the projects to be built
If there is no valid order return an error
(replacing str as presented in the book with nums 0-4 corresponding with alphabetical order)
"""


class Graph:    
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __repr__(self):
        return '\n'.join([f'{n}: {neighbors}' for n, neighbors in enumerate(self.data)])


# implement a breadth first search, if path is invalid returns False, else returns a valid path
def bfs(graph, source):
    # Check for invalid paths
    for connection_list in graph.data:
        for connection in connection_list:
            if connection_list.count(connection) > 1:
                # Returning False in stead of throwing an error
                return False


    # check for correct path if no invalid path is found
    can_go_next = []
    already_seen = []
    visited = [False] * len(graph.data)
    queue = []

    visited[source] = True
    queue.append(source)
    already_seen.append(source)
    i = 0

    while i < len(queue):
        for v in graph.data[queue[i]]:
            for item in graph.data[v]:
                if item not in already_seen:
                    can_go_next.append(item)

            if not visited[v]:
                visited[v] = True
                queue.append(v)
                already_seen.append(v)
        i += 1

    # add missing nodes to the end (meaning they have no prereques and can be placed wherever)
    for n in range(graph.num_nodes):
        if n not in already_seen:
            queue.append(n)

    return queue


# for below examples can use a for loop to check more than one starting node


# correctly returns a correct order (not the same order as the book, but still valid)
num_nodes1 = 6
edges1 = [(0, 3), (5, 1), (1, 3), (5, 0), (3, 2)]
graph1 = Graph(num_nodes1, edges1)
print(bfs(graph1, 5))


# returns False
num_nodes2 = 4
edges2 = [(0, 1), (1, 0), (1, 2), (3, 2), (3, 2)]
graph2 = Graph(num_nodes2, edges2)
print(bfs(graph2, 0))