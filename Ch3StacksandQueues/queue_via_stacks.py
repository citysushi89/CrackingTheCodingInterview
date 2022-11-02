"""
queue_via_stacks.py implements a queue via 2 stacks
"""
import unittest


class MyQueue:
    def __init__(self) -> None:
        self.stack_newest = Stack()
        self.stack_oldest = Stack()

    def add(self, value):
        self.stack_newest.push(value)

    def remove(self):
        while len(self.stack_newest):
            self.stack_oldest.push(self.stack_newest.pop())
        result = self.stack_oldest.pop()
        while len(self.stack_oldest):
            self.stack_newest.push(self.stack_oldest.pop())
        return result


class Stack:
    def __init__(self) -> None:
        self.stack_list = []
        self.stack_size = 0
    
    def __len__(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)
        self.stack_size += 1

    def pop(self):
        if not len(self.stack_list):
            return None
        return self.stack_list.pop()

    def show_stack(self):
        print(self.stack_list)

# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(5)
# stack.show_stack()

class Test(unittest.TestCase):
  def test_queue_via_stacks(self):
    queue = MyQueue()
    queue.add(11)
    queue.add(22)
    queue.add(33)
    self.assertEqual(queue.remove(), 11)
    queue.add(44)
    queue.add(55)
    queue.add(66)
    self.assertEqual(queue.remove(), 22)
    self.assertEqual(queue.remove(), 33)
    self.assertEqual(queue.remove(), 44)
    self.assertEqual(queue.remove(), 55)
    queue.add(77)
    self.assertEqual(queue.remove(), 66)
    self.assertEqual(queue.remove(), 77)
    self.assertEqual(queue.remove(), None)

if __name__ == "__main__":
  unittest.main()