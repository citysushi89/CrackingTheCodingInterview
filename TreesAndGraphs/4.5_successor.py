"""
Finds the 'next' node (in-order successor) of a given node in a binary search tree.
Assuming there are links to its parent
Program currently only prints the successor to the console, issues returning in a recursive function
"""
from StructureTemplates.Trees.binary_search_tree import display_keys

global needed_node, parent_node


class Node:
    def __init__(self, value, left=None, right=None, parent=None):
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


def pre_order_traversal_modified(node, input_node_value):
    if node is None:
        return []

    try:
        if node.value == input_node_value:
            parent_node = node.parent.value
            print(f'The successor is: {parent_node}')
            return parent_node

    except AttributeError:
        pass

    pre_order_traversal_modified(node.left, input_node_value)
    pre_order_traversal_modified(node.right, input_node_value)


def find_successor(input_tree, input_node_value):
    # Iterate through the nodes until the requested Node is found
    return pre_order_traversal_modified(input_tree, input_node_value)



# Setup the Tree
tree1 = insert(None, 10)
ARRAY2 = [5, 15, 2, 6, 11, 16]
for item in ARRAY2:
    insert(tree1, item)

# Prints 10, the parent of 15
find_successor(tree1, 15)
