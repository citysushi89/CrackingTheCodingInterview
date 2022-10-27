# loop_detection.py checks a linked list for a loop and returns the node at the loop


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class linkedList:
    def __init__(self, head=None) -> None:
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

    def check_for_loop(self):
        values = []
        loop_start = ''
        current_node = self.head
        while current_node:
            if current_node.value in values:
                """
                Stores and returns loop start based on its first occurences's node location and value
                Used a str because the double use of append caused issues, can change type if necessary
                """
                loop_start = f'{values.index(current_node.value) + 1}, {current_node.value}'
                return loop_start
            values.append(current_node.value)
            current_node = current_node.next

ll_1 = linkedList()
ll_1.append(1)
ll_1.append(2)
ll_1.append(3)
ll_1.append(4)
ll_1.append(5)
ll_1.append(6)
ll_1.append(4)

print(ll_1.check_for_loop())