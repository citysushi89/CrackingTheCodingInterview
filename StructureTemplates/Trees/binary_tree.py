"""
From Jovian: https://jovian.ai/learn/data-structures-and-algorithms-in-python/lesson/lesson-2-binary-search-trees-traversals-and-balancing/your-notebooks#C147
Can also include a key in the node, but did not intially 
"""
import os


class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def display_keys(node, space='\t', level=0):
    # If empty Node
    if node is None:
        print(space*level + 'NONE')
        return
    
    # If node is a leaf
    if node.left is None and node.right is None:
        print(space*level + str(node.value))
        return

    # If root has children
    display_keys(node.right, space, level + 1)
    print(space*level + str(node.value))
    display_keys(node.left, space, level + 1)

# BST Insertion
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

# Insert to keep binary tree balanced, not to create a bst
def insert_not_bst(node, value):
    if node is None:
        node = Node(value)
    elif tree_height(node.left) < tree_height(node.right):
        node.left = insert_not_bst(node.left, value)
        node.left.parent = node
    else:
        node.right = insert_not_bst(node.right, value)
        node.right.parent = node

def tree_height(node):
    if node is None: 
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


# TO start a BST
tree1 = insert(None, 10)
ARRAY = [8, 12, 9, 7, 13, 11]
for item in ARRAY:
    insert(tree1, item)

