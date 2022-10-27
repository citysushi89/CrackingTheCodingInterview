"""
Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height
"""

SORTED_ARRAY = [1, 2, 3, 4, 5, 6]
SORTED_ARRAY2 = [1, 2, 3, 4, 5, 6, 7]

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


def insert(node, value):
    if node is None:
        node = Node(value)
    elif node.right is None:
        node.right = insert(node.right, value)
        node.right.parent = node
    elif value < node.value:
        node.left = insert(node.left, value)
        node.left.parent = node
    elif value > node.value:
        node.right = insert(node.right, value)
        node.right.parent = node
    return node

def create_balance_bi_search_tree(sorted_arr):
    arr_len = len(sorted_arr)
    root = sorted_arr[arr_len // 2]
    tree = insert(None, root)
    reversed_list = sorted_arr[::-1]
    for item in reversed_list:
        if item != root:
            insert(tree, item)
    return display_keys(tree)


binary_tree_1 = create_balance_bi_search_tree(SORTED_ARRAY)
binary_tree_2 = create_balance_bi_search_tree(SORTED_ARRAY2)
