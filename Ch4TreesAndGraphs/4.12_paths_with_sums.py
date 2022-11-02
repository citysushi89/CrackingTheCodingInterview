"""
Given a binary tree, each node contains an integer, 
design an algorithm that find a given path that sums to a given value
Does not need to start or end at the root or a leaf, but must go downward
"""

class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def tree_height(node):
    if node is None: 
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

def insert_not_bst(node, value):
    if node is None:
        node = Node(value)
    elif tree_height(node.left) < tree_height(node.right):
        node.left = insert_not_bst(node.left, value)
        node.left.parent = node
    else:
        node.right = insert_not_bst(node.right, value)
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

def pre_order_traversal(node, output_list, level):
    if node is None:
        level -= 1
        return []
    else:
        output_list.append(node.value)
    
    # output_list[level].insert(len(output_list[level - 1]), node.value)

    level += 1
    pre_order_traversal(node.left, output_list, level)
    pre_order_traversal(node.right, output_list, level)
    return output_list


# # # # # # # 
def get_sum_path(tree, desired_sum):
    # TODO get the values at each level
    output_list = []
    level = 0
    values = pre_order_traversal(tree1, output_list, level)
    # TODO see if a combination of values, one at each level equal desired_sum


    # TODO then see if the comination is a valid path - will be linear, so return each element and see if its
    # node.next.value = 

    return values

# # # # # # # 


tree1 = insert_not_bst(None, 10)
ARRAY = [8, 12, 9, 7, 13]
for item in ARRAY:
    insert_not_bst(tree1, item)


print(get_sum_path(tree1, 20))
# print(display_keys(tree1))