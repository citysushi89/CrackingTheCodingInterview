# palindrome.py func checks if the given linked list is a palindrome

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

    def get_node_count(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def get_node_value(self, location):
        if location < 1:
            return -1
        current_node = self.head
        while location > 1:
            current_node = current_node.next
            location -= 1
        return current_node.value

    def is_palindrome(self):
        num_nodes = self.get_node_count()
        for i in range(1, num_nodes - 1):
            value_1 = self.get_node_value(i)
            value_2 = self.get_node_value((num_nodes - (i - 1)))
            if value_1 == value_2:
                continue
            else:
                return False
        return True
        
ll_1 = linkedList()
ll_1.append(1)
ll_1.append(2)
ll_1.append(3)
ll_1.append(2)
ll_1.append(1)

ll_2 = linkedList()
ll_2.append(1)
ll_2.append(2)
ll_2.append(3)
ll_2.append(4)
ll_2.append(5)

# Should be true
print(ll_1.is_palindrome())
# Should be false
print(ll_2.is_palindrome())
