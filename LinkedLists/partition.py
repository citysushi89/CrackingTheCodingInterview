# partition.py contains a function partition_by_value that partitions a linked list based on an input value


class Node:
    def __init__(self,  value, next=None):
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


    def partition(self, value):
        # test if the given value (the partition) is greater or less than the given node's value, if given node's value is less than place it after the head, 
        # else connect it to a somewhat temp linked list to be connected when current_node.next is None
        # If equal place to the right list
        ll_right = linkedList()
        ll_left = linkedList()

        # TODO does not work if value is head node for now
        current_node = self.head
        while True:
            if current_node.value < value:
                # Add link to left side
                ll_left.append(current_node.value)
                print(f'cnv: {current_node.value}')
                ll_left_last_node = current_node
                print(f'left left node next::{ll_left_last_node.next}')
            else:
                # Add link to right side
                print(f'over value: {current_node.value}')
                
                ll_right.append(current_node.value)

            # Cycle to the next node
            current_node = current_node.next

            # Process is done, now connect the lists
            if current_node is None:
                # Now to connect the lists
                while True:
                    current_node_right = ll_right.head
                    while True:
                        ll_left.append(current_node_right.value)
                        current_node_right = current_node_right.next

                        if current_node_right is None:
                            return ll_left

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

ll.append(1)
ll.append(4)
ll.append(2)
ll.append(8)
ll.append(10)
ll.append(3)
ll.append(7)
ll.append(4)


ll = ll.partition(8)
print(ll.find_values())
