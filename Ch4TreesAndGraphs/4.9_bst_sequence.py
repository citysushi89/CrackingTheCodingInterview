"""
A binary search tree was created by traversing through an array from left to right and inserting each element, 
given a binary search tree with distinct elements, print all possible arrays that could have led to this tree
# NOTE: works for trees of height 3 and fewer
"""

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

def tree_height(node):
    if node is None: 
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


def print_possible_arrays(head_node, height):
    # Get the head
    possible_arrays = []
    new_array1 = []
    new_array2 = []
    new_array1.append(head_node.value)
    new_array2.append(head_node.value)
    current_node = head_node

    for h in range(1, height):
        print(h)
        new_array1.append(current_node.left.value)
        new_array1.append(current_node.right.value) 
        new_array2.append(current_node.right.value)
        new_array2.append(current_node.left.value) 
        if h != 1:
            length_of_array_to_start = len(possible_arrays) - 1
            for i in range(length_of_array_to_start + 1):

                # make a copy of the list append to the end  each iteration 
                possible_arrays.append(possible_arrays[i])

            for i in range(length_of_array_to_start):
                for t in new_array1:
                    possible_arrays[i].append(t)
                
                for e in new_array2:
                    possible_arrays[i + length_of_array_to_start].append(e)

        else:
            possible_arrays.append(new_array1)
            possible_arrays.append(new_array2)
        new_array1 = []
        new_array2 = []
        current_node = current_node.left
    return possible_arrays
    

# start a BST
tree1 = insert(None, 10)
ARRAY = [8, 12, 9, 7, 13, 11]
# ARRAY = [8, 12, 9, 7, 13, 11, 6, 5, 14, 15]
# ARRAY = [8, 12]
for item in ARRAY:
    insert(tree1, item)
height = tree_height(tree1)


print(print_possible_arrays(tree1, height))