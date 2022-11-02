"""
route_btwn_nodes.py Given a directed graph and two nodes (0 and 4), 
design an alogrithm to see if there is a route between 0 and 4
"""
# TODO third test comes back wrong

from turtle import distance


class Graph:
    def __init__(self, num_nodes, edges, directed=False, weighted=False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]
        for edge in edges:
            if self.weighted:
                node1, node2, weight = edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2]
            else:
                node1, node2 = edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)

    def __repr__(self) -> str:
        result = ''
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.data, self.weight)):
                result += f'{i}: {list(zip(nodes, weights))}\n'
        else:
            for i, nodes in enumerate(self.data):
                result += f'{i}: {nodes}\n'
        return result

    # Just 2 nodes
    def are_they_connected(self, node1, node2):
        for node in self.data:
            if node == [node1]:
                return True
            elif node == [node2]:
                return True
        return False

    def pick_next_node(self, visited):
        min_node = None
        for node in range(len(visited)):
            if not visited[node]:
                min_node = node
        return min_node

    def find_path(self, source, dest):
        visited = [False] * len(self.data)
        queue = []
        idx = 0
        queue.append(source)
        visited[source] = True
        # Need to check here for edges
        nodes_list = []
        for i, nodes in enumerate(self.data):
            nodes_list.append(nodes)
            # print(i, nodes)
        print(nodes_list)
        while idx < len(queue) and not visited[dest]:
            current = queue[idx]
            next_node = self.pick_next_node(visited)
            if next_node is not None:
                visited[next_node] = True
                queue.append(next_node)
            idx += 1
        if visited[source] == True and visited[dest] == True:
            return True
        else:
            return False


# Test with 5 total nodes and with 2 total nodes - should be True
num_nodes1 = 5
edges1 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]
graph1 = Graph(num_nodes1, edges1, directed=True)
print(graph1.find_path(0, 4))

# Testing with literally just two nodes - should be True
num_nodes2 = 2
edges2 = [(0, 1)]
graph2 = Graph(num_nodes2, edges2, directed=True)
print(graph2.find_path(0, 1))

# TODO below is currently incorrect
# Testing with literally just two nodes - should be False
num_nodes3 = 2
edges3 = []
graph3 = Graph(num_nodes3, edges3, directed=True)
print(graph3.find_path(0, 1))
