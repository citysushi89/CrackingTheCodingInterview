"""
Given a Binary Tree, design an algorithm which creates a linked list of all the nodes at each depth
TODO IN PROGRESS
"""

# TODO create Binary Tree
class Node:
    def __init__(self, value, left=None, right=None, parent=None) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def insert(node, value):
    if node is None:
        node = Node(value)
    elif value < node.value:
        node.left = insert(node.left, value)
        node.left.parent = node
    elif value > node.value:
        node.right = insert(node.right, value)
        node.right.parent = node
    return node

def display_keys(node, space='\t', level=0):
    if node is None:
        print(space*level + 'None')
        return
    
    if node.left is None and node.right is None:
        print(space*level + str(node.value))
        return
    
    display_keys(node.right, space, level + 1)
    print(space*level + str(node.value))
    display_keys(node.left, space, level + 1)

ARRAY = [1, 3, 2, 5, 6, 4]

tree = insert(None, 0)
for item in ARRAY:
    insert(tree, item)

display_keys(tree)

# TODO create algo that gets the nodes at each depth
def get_nodes_at_depth():

# TODO create a linked list based on those nodes