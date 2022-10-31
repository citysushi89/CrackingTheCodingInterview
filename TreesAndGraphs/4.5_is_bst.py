"""
Implement a function to check if a tree is a binary search tree
NOTE: currently throws an except if the passed-in tree is not a bst, Returns true if it is a bst
"""
from StructureTemplates.Trees.binary_search_tree import display_keys


class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# Technically a BST insertion
def insert_bst(node, value):
    if node is None:
        node = Node(value)
    elif value < node.value:
        node.left = insert_bst(node.left, value)
        node.left.parent = node
    elif value > node.value:
        node.right = insert_bst(node.right, value)
        node.right.parent = node
    return node


def insert_regular(node, value):
    if node is None:
        node = Node(value)
    elif node.left is None:
        node.left = insert_regular(node.left, value)
        node.left.parent = node
    elif node.right is None:
        node.right = insert_regular(node.right, value)
        node.right.parent = node
    return node


# TODO add function to check if binary tree
def is_bst(node, which_side=None):
    if node is None:
        return []
    if node is not None:
        # node has children
        if node.right and node.left:
            if node.value < node.right.value and node.value > node.left.value:
                pass
            else:
                raise Exception("Not a bst.")

        elif node.right:
            if node.value < node.right.value:
                pass
            else:
                raise Exception("Not a bst.")

        elif node.left:
            pass
            if node.value > node.left.value:
                pass
            else:
                raise Exception("Not a bst.")

        # Node does not have children
        else:
            if node.value < node.parent.value and which_side == 'right':
                raise Exception("Not a bst.")
            elif node.value > node.parent.value and which_side == 'left':
                raise Exception("Not a bst.")

    is_bst(node.left)
    is_bst(node.right)
    return True

# Will throw error (not a bst)
tree1 = insert_regular(None, 5)
ARRAY = [1, 4]
for item in ARRAY:
    insert_regular(tree1, item)
# print(is_bst(tree1))

# Will return True (is a bst)
tree2 = insert_bst(None, 10)
ARRAY2 = [5, 15, 2, 6, 11, 16]
for item in ARRAY2:
    insert_bst(tree2, item)
print(is_bst(tree2))
