"""
stack_of_plates.py contains a stack that, when exceeding a threshold, creates a new stack
"""


class MultiStack():
  def __init__(self, capacity):
    self.capacity = capacity
    self.stacks = []
  
  def push(self, item):
    if len(self.stacks) and (len(self.stacks[-1])) < self.capacity:
      self.stacks[-1].append(item)
    else:
      self.stacks.append([item])
  
  def pop(self):
    while len(self.stacks) and len(self.stacks[-1]) == 0:
      self.stacks.pop()
    if len(self.stacks) == 0:
      return None
    else:
      return self.stacks[-1].pop()    
  
  def pop_at(self, stack_number):
    if len(self.stacks[stack_number]) > 0:
      return self.stacks[stack_number].pop()
    else:
      return None

import unittest

class Test(unittest.TestCase):
  def test_multi_stack(self):
    stack = MultiStack(3)
    stack.push(11)
    stack.push(22)
    stack.push(33)
    stack.push(44)
    stack.push(55)
    stack.push(66)
    stack.push(77)
    stack.push(88)
    self.assertEqual(stack.pop(), 88)
    self.assertEqual(stack.pop_at(1), 66)
    self.assertEqual(stack.pop_at(0), 33)
    self.assertEqual(stack.pop_at(1), 55)
    self.assertEqual(stack.pop_at(1), 44)
    self.assertEqual(stack.pop_at(1), None)
    stack.push(99)
    self.assertEqual(stack.pop(), 99)
    self.assertEqual(stack.pop(), 77)
    self.assertEqual(stack.pop(), 22)
    self.assertEqual(stack.pop(), 11)
    self.assertEqual(stack.pop(), None)

if __name__ == "__main__":
  unittest.main()

