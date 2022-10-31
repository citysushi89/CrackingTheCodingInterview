
# In order traversal
def traverse_in_order(node):
    if node is None: 
        return []
    return(traverse_in_order(node.left) + 
           [node.key] + 
           traverse_in_order(node.right))


def pre_order_traversal(node):
    if node is None:
        return []

    pre_order_traversal(node.left)
    pre_order_traversal(node.right)