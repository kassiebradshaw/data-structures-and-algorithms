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
  empty_stack = Stack()
  empty_stack.push("puppy")
  actual = empty_stack.top.value
  expected = "puppy"
  assert actual == expected

def test_push_multiple_nodes_to_stack():
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

# def test_pop_off_empty_stack():
#   new_stack = Stack()
#   actual = new_stack.pop()
#   expected = 'Stack is empty'
#   assert actual == expected

def test_pop_off_stack():
  new_stack = Stack()
  new_stack.push("first node")
  new_stack.push("second node")
  new_stack.push("third node")

  actual = new_stack.pop()
  expected = "third node"

  assert actual == expected

def test_multiple_pops():
  new_stack = Stack()
  new_stack.push("H")
  new_stack.push("E")
  new_stack.push("L")
  new_stack.push("L")
  new_stack.push("O")

  actual_first_pop = new_stack.pop()
  actual_second_pop = new_stack.pop()
  actual_third_pop = new_stack.pop()

  expected_first_pop = "O"
  expected_second_pop = "L"
  expected_third_pop = "L"

  assert actual_first_pop == expected_first_pop
  assert actual_second_pop == expected_second_pop
  assert actual_third_pop == expected_third_pop

def test_stack_isEmpty():
  new_stack = Stack()
  actual = new_stack.isEmpty()
  expected = True
  assert actual == expected

def test_stack_is_not_empty():
  new_stack = Stack()
  new_stack.push("Hello from the stack!")

  actual = new_stack.isEmpty()
  expected = True
  assert actual != expected

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

def test_add_node_to_queue():
  new_queue = Queue()
  new_queue.enqueue('kitty')

  actual = new_queue.front.value
  expected = 'kitty'
  assert actual == expected

def test_add_multiple_nodes_to_queue():
  new_queue = Queue()
  new_queue.enqueue('kitty')
  new_queue.enqueue('puppy')
  new_queue.enqueue('fishy')
  new_queue.enqueue('bunny')

  actual_front = new_queue.front.value
  expected_front = 'kitty'
  actual_back = new_queue.back.value
  expected_back = 'bunny'

  assert actual_front == expected_front
  assert actual_back == expected_back

def test_remove_node_from_queue():
  new_queue = Queue()
  new_queue.enqueue('kitty')
  new_queue.enqueue('puppy')
  new_queue.enqueue('fishy')
  new_queue.enqueue('bunny')

  actual = new_queue.dequeue()
  expected = 'kitty'

  assert actual == expected
