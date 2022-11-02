# remove_duplicates.py 
# NOT DONE: find_values returning a lot when used in remove_dups --> and remove_dups still does not have the actual deletion part (could be a different function)

from turtle import position


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
        
    # Gets index in a linked list, so need to +1 for the index in a regular list
    def get_index(self, value):
        indexes = []
        print(value)
        counter = 1
        current = self.head 
        while current.next is not None:
            if value == current.value:
                indexes.append(counter)
                counter += 1
            current = current.next 

        if value == current.value:
            indexes.append(counter)
            counter += 1
        return indexes


    def remove_dups(self):
        values = self.find_values()
        indexes_to_remove = []
        print(values)
        for value in values:

            occurences = values.count(value)
            if occurences == 1:
                pass
            elif occurences > 1:
                index_and_occurence = self.get_index(value) 
                indexes_to_remove.append(index_and_occurence)
                pass

        return indexes_to_remove


ll = linkedList()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(3)
ll.append(4)
ll.append(4)
# print(ll)
print(ll.remove_dups())
