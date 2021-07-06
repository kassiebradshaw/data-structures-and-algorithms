import unittest
from code_challenges.stack_and_queue.stack_and_queue import Node, Stack, Queue


### ----- Starter Tests ----- ###
# To make sure pytest and imports are working

def test_node():
  assert Node

def test_node_value():
  test_node = Node(1)
  actual = test_node.value
  expected = 1
  assert actual == expected

def test_next_node():
  node3 = Node("guava")
  node2 = Node("grape", node3)
  node1 = Node("apple", node2)
  actual1 = node1.next.value
  expected1 = "grape"
  actual2 = node1.next.next.value
  expected2 = "guava"
  assert actual1 == expected1
  assert actual2 == expected2

def test_stack():
  assert Stack

def test_queue():
  assert Queue

### ----- Stack Tests ----- ###

def test_empty_stack():
  # README test #6
  empty_stack = Stack()

  actual = empty_stack.top
  expected = None
  assert actual == expected

def test_push_to_empty_stack():
  # README test #1
  empty_stack = Stack()
  empty_stack.push("puppy")
  actual = empty_stack.top.value
  expected = "puppy"
  assert actual == expected

def test_push_multiple_nodes_to_stack():
  # README test #2
  new_stack = Stack()
  new_stack.push("first node")
  new_stack.push("second node")
  new_stack.push("third node")

  actual_last_push = new_stack.top.value
  expected_last_push = "third node"

  actual_second_push = new_stack.top.next.value
  expected_second_push = "second node"

  actual_first_push = new_stack.top.next.next.value
  expected_first_push = "first node"

  assert actual_first_push == expected_first_push
  assert actual_second_push == expected_second_push
  assert actual_last_push == expected_last_push

def test_pop_off_empty_stack():
  new_stack = Stack()
  actual = new_stack.pop()
  expected = 'Stack is empty'
  assert actual == expected

# def test_pop_off_stack():
#   new_stack = Stack()
#   new_stack.push("first node")
#   new_stack.push("second node")
#   new_stack.push("third node")

#   actual = new_stack.pop()
#   expected = "third node"

#   assert actual == expected



### ----- Queue Tests ----- ###

def test_empty_queue():
  # README test #13
  empty_queue = Queue()

  actual_front = empty_queue.front
  expected_front = None

  actual_back = empty_queue.back
  expected_back = None

  assert actual_front == expected_front
  assert actual_back == expected_back
