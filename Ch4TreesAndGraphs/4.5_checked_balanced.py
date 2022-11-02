"""
Implement a function to check if a binary tree is balanced
(For the purposes of this question, a balanced tree is defiend to be a tree such that 
the heights of the two subtrees of any node never differ by more than one)
"""

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
    elif value <node.value:
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




def check_balanced(tree):
    # Get each node and check its height

    pass


tree1 = insert(None, 0)
ARRAY = [1, 3, 2, 5, 4, 6]
for item in ARRAY:
    insert(tree1, item)
print(display_keys(tree1))


print(check_balanced(tree1))