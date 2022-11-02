
"""
How would you design a stack in which, in addition to push and pop, has a function min which returns the minimum element?
Push Pop and Min should all operate in O(1) time
"""
 
# Store the minimum vakue while initializig each node
 
 
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
 
 
class Stack:
    def __init__(self):
        self.top = None
        self.stack_size = 0
        self.min = None
 
    def push(self, value):
        node = Node(value)
 
        if self.top is None:
            self.top = node
            self.stack_size += 1
            # Store minimums while pushing each node so they can be fetched as an O(1) operation
            self.min = node.value
        else:
            node.next = self.top
            self.top = node
            self.stack_size += 1

            # Store minimums while pushing each node so they can be fetched as an O(1) operation
            if node.value < self.min:
                self.min = node.value
 
    def pop(self):
        current_node = self.top.next
        self.top = current_node
        self.stack_size -=1
    
    def find_min(self):
        return self.min

 
stack = Stack()
 
 
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.find_min())