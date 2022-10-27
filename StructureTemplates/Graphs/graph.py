"""
filled in with graph from Jovian
https://hub.binder.jovian.ai/user/owenpickard89/api-git-de03faa-109fb84a9d886_1-rwyahgw2/notebooks/python-graph-algorithms.ipynb
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
        
    def __str__(self):
        return self.__repr__()
    
    # Write a function to add an edge to a graph represented as an adjacency list.
    # to call: graph1.add_edge([(2, 4)])
    def add_edge(self, new_edges):
        for n1, n2 in new_edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
            
    # Write a function to remove an edge from a graph represented as a adjacency list.
    # to call: graph1.remove_edge([(0, 1)])
    def remove_edge(self, edge_to_rm):
        first_edge = edge_to_rm[0][0]
        second_edge = edge_to_rm[0][1]
        self.data[first_edge].remove(second_edge)
        self.data[second_edge].remove(first_edge)
        