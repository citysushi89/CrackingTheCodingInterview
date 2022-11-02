"""
filled in with graph from Jovian:
allows for weighed and directed graphs
https://hub.binder.jovian.ai/user/owenpickard89/api-git-de03faa-109fb84a9d886_1-rwyahgw2/notebooks/python-graph-algorithms.ipynb
"""

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
                    self.weight[node2].append(weight)
            else:
                node1, node2 = edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)
                        
    def __repr__(self):
        result = ''
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.data, self.weight)):
                result += f'{i}: {list(zip(nodes, weights))}\n'
        else:
            for i, nodes in enumerate(self.data):
                result += f'{i}: {nodes}\n'
        return result
            

# Making a graph with weights
num_nodes5 = 9
edges5 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6), 
          (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]
graph5 = Graph(num_nodes5, edges5, weighted=True)