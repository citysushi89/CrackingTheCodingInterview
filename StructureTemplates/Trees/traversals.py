
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


# pre order traversal with output of every node value
def pre_order_traversal(node, output_list):
    if node is None:
        return []
    else:
        output_list.append(node.value)

    pre_order_traversal(node.left, output_list)
    pre_order_traversal(node.right, output_list)
    return output_list