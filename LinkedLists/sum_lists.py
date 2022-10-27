# sum_lists.py contains two different linked lists that represent numbers, the task is to get the values, reverse them, then add them


class Node:
    def __init__(self, value, next=None):
        self.value = value 
        self.next = next


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, value):
        node = Node(value)
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
        values = ''
        current_node = self.head
        while current_node is not None:
            values += str(current_node.value)
            current_node = current_node.next
        return values



def sum_lists(list_1, list_2):
    values_1 = list_1[::-1]
    values_2 = list_2[::-1]
    return int(values_1) + int(values_2)


ll_1 = linkedList()
ll_1.append(3)
ll_1.append(2)
ll_1.append(1)
ll_2 = linkedList()
ll_2.append(6)
ll_2.append(5)
ll_2.append(4)

list_1 = ll_1.get_values()
list_2 = ll_2.get_values()

# Should equal 123 + 456 = 579
print(sum_lists(list_1, list_2))

