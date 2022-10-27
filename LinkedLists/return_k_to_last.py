# return_k_to_last.py func returns the kth to last element in a singly linked list

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class linkedList:
    def __init__(self, head=None):
        self.head = head
        pass

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
    
        currentNode = self.head
        while True:
            if currentNode.next is None:
                currentNode.next = node
                break
            currentNode = currentNode.next

    def count_nodes(self):
        count = 0
        if self.head is None:
            return 0
        current_node = self.head
        while current_node.next is not None:
            count += 1
            current_node = current_node.next
        count += 1
        return count
    
    def get_value_at_position(self, index):
        current_node = self.head
        while index > 0:
            current_node = current_node.next
            index -= 1
        return current_node.value

    def return_k_to_last(self, k_to_last):
        num_nodes = self.count_nodes()
        index_needed = num_nodes - k_to_last
        if index_needed < 0:
            return f"Please use a number within the range of the list. The current list has {num_nodes} nodes."
        k_node = self.get_value_at_position(index_needed)
        return k_node


ll = linkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)

# Second to last element, is 5
print(ll.return_k_to_last(2))

# First element, is 1
print(ll.return_k_to_last(6))


