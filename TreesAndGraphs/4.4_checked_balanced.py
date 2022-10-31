"""
If no exception is thrown
Implement a function to check if a binary tree is balanced
(For the purposes of this question, a balanced tree is defined to be a tree such that
the heights of the two subtrees of any node never differ by more than one)
NOTE: currently throws an exception when the tree is not balanced
"""
from StructureTemplates.Trees.binary_search_tree import display_keys


class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# Technically a BST insertion      
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


def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


def pre_order_traversal(node, level, previous_height):
    if node is None:
        level -= 1
        return []
    level += 1
    height = tree_height(node)
    if abs(height - previous_height) > 1:
        raise Exception("Tree not balanced and this is how I am exiting recurion for now.")

    previous_height = height
    pre_order_traversal(node.left, level, previous_height)
    pre_order_traversal(node.right, level, previous_height)


tree1 = insert(None, 0)
ARRAY = [1, 3, 2, 5, 4, 6]
for item in ARRAY:
    insert(tree1, item)
level1 = tree_height(tree1)

tree2 = insert(None, 5)
# ARRAY2 = [1, 2, 3, 4, 5, 6]
ARRAY2 = [7, 3, 2, 4, 8, 6]
for item in ARRAY2:
    insert(tree2, item)
level2 = tree_height(tree2)


# Should return Thrown Error
# print(pre_order_traversal(tree1, level1, previous_height=level1))

# Should return None (Tree is balanced)
print(pre_order_traversal(tree2, level2, previous_height=level2))
