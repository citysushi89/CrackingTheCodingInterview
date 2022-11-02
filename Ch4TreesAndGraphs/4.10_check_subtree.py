"""
T1 and T2 are two very large binary trees, with T1 much bigger than T2. 
Create an algo to determine if t2 is a subtree of T1
"""

global condition 
condition = False

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


def pre_order_traversal_single_output(node, sub_tree_head, output_list):
    if node is None:
        return []
    # List is the only data type returning in a recursive loop at the moment
    if node.value == sub_tree_head.value:
        output_list.append(node.value)
        output_list.append(node)
    pre_order_traversal_single_output(node.left, sub_tree_head, output_list)
    pre_order_traversal_single_output(node.right, sub_tree_head, output_list)
    return output_list

def pre_order_traversal_check_list_output(node, output_list):
    if node is None:
        return []
    # List is the only data type returning in a recursive loop at the moment
    output_list.append(node.value)
    pre_order_traversal_check_list_output(node.left, output_list)
    pre_order_traversal_check_list_output(node.right, output_list)
    return output_list
    
    
def check_if_subtree(larger_tree, potential_sub_tree):
    sub_tree_head = potential_sub_tree
    output_list = []
    list_of_nodes = pre_order_traversal_single_output(larger_tree, sub_tree_head, output_list)
    if list_of_nodes:
        matching_node_value = list_of_nodes[0]
        matching_node = list_of_nodes[1]
    else:
        return False
    
    if sub_tree_head.value == matching_node_value:
        t1_placeholder = []
        t2_placeholder = []
        t1_list = pre_order_traversal_check_list_output(matching_node, t1_placeholder)
        t2_lsit = pre_order_traversal_check_list_output(sub_tree_head, t2_placeholder)
        if t1_list == t2_lsit:
            return True
        else:
            return False
    else:
        return False
    

# Tree setups
tree1 = insert(None, 10)
ARRAY = [8, 12, 9, 7, 13, 11]
for item in ARRAY:
    insert(tree1, item)

tree2 = insert(None, 8)
ARRAY2 = [7, 9]
for item in ARRAY2:
    insert(tree2, item)

tree3 = insert(None, 15)
ARRAY3 = [14, 16]
for item in ARRAY3:
    insert(tree3, item)

# Should be True
print(check_if_subtree(tree1, tree2))
# Should be False
print(check_if_subtree(tree1, tree3))

