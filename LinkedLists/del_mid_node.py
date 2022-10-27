# del_mid_node.py remove_node removes an given node if the node is not the first or last node


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            return 

        current_node = self.head
        while True:
            if current_node.next is None:
                current_node.next = node
                break
            current_node = current_node.next

    def remove_node(self, node_pos):

        # Does not remove head node and cannot remove negative index
        if node_pos < 2:
            return 'Cannot remove the head node nor an negative index'

        current_node = self.head
        while True:
            if current_node.next is None:
                return 'Cannot remove the last node (per question restrictions)'
            if node_pos == 1:
                # Skip the pointer from current node
                last_node.next = current_node.next
                break
            last_node = current_node
            current_node = current_node.next
            node_pos -= 1

    # Used to ensure remove_node was successful
    def find_values(self):
        value_list = []
        current_node = self.head
        while True:
            # Need to include this last one as well
            if current_node.next is None:
                value_list.append(current_node.value)
                return value_list
            else:
                value_list.append(current_node.value)
                current_node = current_node.next


ll = linkedList()

ll.append(2)
ll.append(4)
ll.append(6)
ll.append(8)
ll.append(10)
ll.append(12)

# Remove node based on position
print(ll.remove_node(3))
print(ll.find_values())