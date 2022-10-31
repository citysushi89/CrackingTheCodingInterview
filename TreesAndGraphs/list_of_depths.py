"""
Given a Binary Tree, design an algorithm which creates a linked list of all the nodes at each depth
TODO IN PROGRESS
"""

# Create linked list
class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append_to_ll(self, value):
        node = LinkedListNode(value)
        self.value = value

        if self.head is None:
            self.head = node
            return

        current_node = self.head
        while True:
            if current_node.next is None:
                current_node.next = node
                break
            current_node = current_node.next

    def get_values(self):
        try:
        # if self.head:
            values = ''
            current_node = self.head
            while current_node is not None:
                values += str(current_node.value)
                current_node = current_node.next
            return values
        except AttributeError: 
            return "None"


# Create a binary Tree
class Node:
    def __init__(self, value, left=None, right=None, parent=None) -> None:
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

# Use to check what the tree looks like
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

def pre_order_traversal(node, level, list_of_linked_lists):
    if node is None:
        level -= 1
        return []
    level += 1
    try:
        node
        list_of_linked_lists[level].append_to_ll(node.value)
    except TypeError:
        pass

    # traverse left subtree
    pre_order_traversal(node.left, level, list_of_linked_lists)
    #traverse right subtree
    pre_order_traversal(node.right, level, list_of_linked_lists)

# Binary Tree
tree1 = insert(None, 0)
ARRAY = [1, 3, 2, 5, 4, 6]
for item in ARRAY:
    insert(tree1, item)

# Set up inputs for the traversal
level = 0
height_of_tree = tree_height(tree1) + 1
list_of_linked_lists = [LinkedList() for _ in range(height_of_tree)]

# Conduct Traversal
print(pre_order_traversal(tree1, level, list_of_linked_lists))

# Check that everything executed correctly
for linked_list in list_of_linked_lists:
    print(LinkedList.get_values(linked_list))
