"""
Implement a BST with functions: insert, find, delete, and get random, which return a random node
"""
import random

class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    # Returns value, parent, left, right
    def find(self, node_value):
        current_node = self.value
        if current_node == node_value:
            return current_node, self.parent, self.left, self.right    
        elif node_value > current_node:
            return self.right.find(node_value)
        elif node_value < current_node:
            return self.left.find(node_value)
        else:
            return -1


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


def delete(tree, node_value):
    found_value, found_parent, found_left, found_right = tree.find(node_value)
    if not found_value:
        return -1

    # replace parent
    # is on the right
    if found_value > found_parent.value:
        found_parent.right = found_right
        found_left.parent = found_right
        found_parent.right.left = found_left
    # is on the left
    else:
        found_parent.left = found_left
        found_right.parent = found_left
        found_parent.left.right = found_right


    
    pass

def tree_height(node):
    if node is None: 
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


def get_random(tree):
    # TODO get the height of the tree
    height = tree_height(tree) - 1
    chosen_height = random.randint(0, height)
    current_node = tree
    while chosen_height > 0:
        left_or_right = random.randint(1, 2)
        if left_or_right == 1:
            current_node = current_node.left
        else:
            current_node = current_node.right
        chosen_height -= 1
    
    if current_node.value is not None:
        return current_node.value
    else:
        return -1

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


tree1 = insert(None, 10)
ARRAY = [8, 12, 9, 7, 13, 11]
for item in ARRAY:
    insert(tree1, item)

# display trees for testing delete

# print(display_keys(tree1))
print(tree1.find(12))
print(delete(tree1, 8))
# print(display_keys(tree1))
print(get_random(tree1))