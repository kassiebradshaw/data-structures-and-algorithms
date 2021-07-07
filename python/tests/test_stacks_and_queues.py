import pytest
from code_challenges.stack_and_queue.stack_and_queue import Node, Stack, Queue, CustomError


### ----- Starter Tests ----- ###
# To make sure pytest and imports are working

def test_node():
  assert Node

# ---------------

def test_node_value():
  test_node = Node(1)
  actual = test_node.value
  expected = 1
  assert actual == expected

# ---------------

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

# ---------------

def test_stack():
  assert Stack

# ---------------

def test_queue():
  assert Queue

### ----- Stack Tests ----- ###

def test_empty_stack(empty_stack):
  actual = empty_stack.top
  expected = None
  assert actual == expected

# ---------------

def test_push_to_empty_stack(empty_stack):
  empty_stack.push("puppy")
  actual = empty_stack.top.value
  expected = "puppy"
  assert actual == expected

# ---------------

def test_push_multiple_nodes_to_stack(empty_stack):
  empty_stack.push("first node")
  empty_stack.push("second node")
  empty_stack.push("third node")

  actual_last_push = empty_stack.top.value
  expected_last_push = "third node"

  actual_second_push = empty_stack.top.next.value
  expected_second_push = "second node"

  actual_first_push = empty_stack.top.next.next.value
  expected_first_push = "first node"

  assert actual_first_push == expected_first_push
  assert actual_second_push == expected_second_push
  assert actual_last_push == expected_last_push

# ---------------

def test_pop_off_empty_stack(empty_stack):
  with pytest.raises(CustomError) as e:
    empty_stack.pop()
    assert str(e.value) == "Stack is empty! No node to pop."
  
# ---------------

def test_pop_off_stack(sample_stack):
  actual = sample_stack.pop()
  expected = "third node"
  assert actual == expected

# ---------------

def test_multiple_pops(sample_stack):

  actual_first_pop = sample_stack.pop()
  actual_second_pop = sample_stack.pop()
  actual_third_pop = sample_stack.pop()

  expected_first_pop = "third node"
  expected_second_pop = "second node"
  expected_third_pop = "first node"

  assert actual_first_pop == expected_first_pop
  assert actual_second_pop == expected_second_pop
  assert actual_third_pop == expected_third_pop

# ---------------

def test_peek(sample_stack):
  actual = sample_stack.peek()
  expected = "third node"
  assert actual == expected

# ---------------

def test_peek_empty_stack(empty_stack):
    with pytest.raises(CustomError) as e:
      empty_stack.peek()
      assert str(e.value) == "Stack is empty! Can't peek."
    
# ---------------

def test_stack_isEmpty(empty_stack):
  actual1 = empty_stack.isEmpty()
  actual2 = empty_stack.isEmpty()
  expected1 = True
  expected2 = False
  assert actual1 == expected1
  assert actual2 != expected2

# ---------------

def test_push_then_pop_then_isEmpty():
  new_stack = Stack()
  new_stack.push('Howdy!')
  
  actual_push = new_stack.top.value
  expected_push = 'Howdy!'
  assert actual_push == expected_push
  actual_pop = new_stack.pop()
  expected_pop = 'Howdy!'
  assert actual_pop == expected_pop
  actual_isEmpty = new_stack.isEmpty()
  expected_isEmpty = True
  assert actual_isEmpty == expected_isEmpty

def test_pop_then_empty(sample_stack):
  with pytest.raises(CustomError) as e:
    sample_stack.pop()
    sample_stack.pop()
    sample_stack.pop()
    sample_stack.pop()
    assert str(e.value) == "Stack is empty! No node to pop."

### ----- Queue Tests ----- ###

def test_empty_queue(empty_queue):
  actual_front = empty_queue.front
  expected_front = None

  actual_back = empty_queue.back
  expected_back = None

  assert actual_front == expected_front
  assert actual_back == expected_back

# ---------------

def test_add_node_to_queue(empty_queue):
  empty_queue.enqueue('kitty')
  actual = empty_queue.front.value
  expected = 'kitty'
  assert actual == expected

# ---------------

def test_add_multiple_nodes_to_queue(empty_queue):
  empty_queue.enqueue('kitty')
  empty_queue.enqueue('puppy')
  empty_queue.enqueue('fishy')
  empty_queue.enqueue('bunny')

  actual_front = empty_queue.front.value
  expected_front = 'kitty'
  actual_back = empty_queue.back.value
  expected_back = 'bunny'

  assert actual_front == expected_front
  assert actual_back == expected_back

# ---------------

def test_remove_node_from_queue(sample_queue):
  actual = sample_queue.dequeue()
  expected = 'kitty'

  assert actual == expected

# ---------------

def test_dequeue_specific_value(sample_queue):
  actual = ""
  expected = "fishy"

  while actual != expected:
    actual = sample_queue.dequeue()

  assert actual == expected


### ------- FIXTURES ------- ###

@pytest.fixture
def empty_stack():
  new_stack = Stack()
  return new_stack

# ----------

@pytest.fixture
def empty_queue():
  new_queue = Queue()
  return new_queue

# ----------

@pytest.fixture
def sample_stack():
  new_stack = Stack()
  new_stack.push("first node")
  new_stack.push("second node")
  new_stack.push("third node")
  return new_stack

# ----------

@pytest.fixture
def sample_queue():
  new_queue = Queue()
  new_queue.enqueue("kitty")
  new_queue.enqueue("puppy")
  new_queue.enqueue("fishy")
  new_queue.enqueue("bunny")

  return new_queue
