### --------------- NODE CLASS CODE --------------- ###

class Node:

  def __init__(self, value, next=None):
    """
    Creates a node instance
    """
    self.value = value
    self.next = next


### --------------- CUSTOM EXCEPTION CLASS CODE --------------- ###

class CustomError(Exception):
  """
  Creates a custom error Exception
  """
  pass


### --------------- STACK CLASS CODE --------------- ###    

class Stack:

  def __init__(self, top=None):
    """
    Creates a stack instance with an empty "top"
    """
    self.top = top

# ---------------------

  def push(self, value):
    """
    Pushes a node with the value parameter
    to the top of the stack
    """

    new_node = Node(value)

    if self.top is None:
      self.top = new_node
    else:
      new_node.next = self.top
      self.top = new_node

# ---------------------

  def pop(self):
    """
    Returns value of node at top of stack,
    removes node from stack, and 
    reassigns top of stack to next node.
    If stack is empty, raises an exception.
    """

    if self.isEmpty():
      raise CustomError("Stack is empty! No node to pop.")
    
    popped_node = self.top
    self.top = popped_node.next
    return popped_node.value

# ---------------------
  
  def peek(self):
    """
    Returns value of node at top of stack.
    """

    if self.isEmpty():
      raise CustomError("Stack is empty! Can't peek.")

    peeked_node = self.top
    return peeked_node.value

# ---------------------
  
  def isEmpty(self):
    """
    Returns True if stack is empty, otherwise returns False
    """
    
    if self.top is None:
      return True
    else:
      return False

### --------------- QUEUE CLASS CODE --------------- ###

class Queue:

  def __init__(self, front=None, back=None):
    """
    Creates a queue instance with empty "front" and "back" values
    """
    
    self.front = front
    self.back = back

# ---------------------

  def enqueue(self, value):
    """
    Creates a node of the value and adds it to the back of the queue.
    If queue is empty, it will set as front.
    """

    new_node = Node(value)
    if self.front is None:
      self.front = new_node
      self.back = new_node
    else:
      self.back.next = new_node
      self.back = new_node

# ---------------------

  def dequeue(self):
    """
    Returns the value of the node at the front of the queue.
    Removes the node from the queue.
    Reassigns "front" to next node in queue.
    Raises an exception if queue is empty.
    """

    if self.isEmpty():
      raise CustomError("Queue is empty! No node to dequeue.")

    dequeued_node = self.front
    self.front = dequeued_node.next
    return dequeued_node.value

# ---------------------

  def peek(self):
    """
    Returns value of node at front of queue.
    """
    if self.isEmpty():
      raise CustomError("Queue is empty! Can't peek.")
    
    peeked_node = self.front
    return peeked_node.value

# ---------------------
  
  def isEmpty(self):
    """
    Returns True if queue is empty, otherwise returns False
    """
    
    if self.front is None:
      return True
    else:
      return False
