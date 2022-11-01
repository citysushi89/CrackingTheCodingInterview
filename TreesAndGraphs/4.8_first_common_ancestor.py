"""
Find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure.
Not necessarily a binary Tree
"""
global parents 

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

# Starts recording when node.left is none
def traverse_in_order(node, target_node_value, parents, height_of_tree):
    if node is None: 
        return []

    try:
        if node.value == target_node_value:
            current_node = node.parent
            while current_node is not None:
                parents.append(current_node.value)
                current_node = current_node.parent

    except AttributeError:
        pass

    return(traverse_in_order(node.left, target_node_value, parents, height) + 
        [node.value] + 
        traverse_in_order(node.right, target_node_value, parents, height))

def find_ancestor(tree, node1_value, node2_value, height):
    parents = []
    traverse_in_order(tree, node1_value, parents, height)
    traverse_in_order(tree, node2_value, parents, height)
    shared_parents = []
    for p in parents:
        if parents.count(p) > 1:
            shared_parents.append(p)

    # If there are more than one set of shared parents, the first item in the list is the earliest shared parent,
    # as the traversal is in order so even if the node are not on the same level the first parent node appended will be 
    # the farthest down the tree of all the parents
    return shared_parents[0]

def tree_height(node):
    if node is None: 
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

# start a tree
tree1 = insert(None, 4)
ARRAY = [8, 6, 3, 7, 1, 2, 9]
for item in ARRAY:
    insert(tree1, item)
height = tree_height(tree1)
print(display_keys(tree1))
# Should be 8
print(find_ancestor(tree1, 6, 9, height))

# Should be 3
print(find_ancestor(tree1, 1, 2, height))