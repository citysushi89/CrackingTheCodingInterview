"""
intersection.py func returns the node at which two linked lists intersect
For the purposes here defining intersection as having the same value at the same node location, 
different from what the book said
"""

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
    
    def get_values(self):
        values = []
        current_node = self.head
        while current_node:
            values.append(current_node.value)
            current_node = current_node.next
        return values

def find_intersection(list1, list2):
    """
    Get values from list 1 and compare to value in list 2
    Faster to iterate over every linked list once and then reference in a regular list 
    as opposed to traversing each linked list for each comparison
    """
    intersections = []
    values1 = list1.get_values()
    values2 = list2.get_values()
    for i in range(len(values1)):
        if values1[i] == values2[i]:
            intersections.append((i, values1[i]))
    # Returns a list of tuples with (linked list node location, value at node location)
    return intersections


ll_1 = linkedList()
ll_1.append(1)
ll_1.append(2)
ll_1.append(3)
ll_1.append(4)
ll_1.append(5)
ll_1.append(6)

ll_2 = linkedList()
ll_2.append(10)
ll_2.append(11)
ll_2.append(12)
ll_2.append(4)
ll_2.append(13)
ll_2.append(16)

print(find_intersection(ll_1, ll_2))