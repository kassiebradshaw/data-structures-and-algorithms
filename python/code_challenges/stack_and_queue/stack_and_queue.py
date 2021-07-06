### --------------- NODE CLASS CODE --------------- ###

class Node:

  def __init__(self, value, next=None):
    """
    Creates a node instance
    """
    self.value = value
    self.next = next

### --------------- STACK CLASS CODE --------------- ###    

class Stack:

  def __init__(self, top=None):
    """
    Creates a stack instance with an empty "top"
    """
    self.top = top


  def push(self, value):
    """
    Pushes a node with the value parameter to the top of the stack
    """
    new_node = Node(value)

    if self.top is None:
      self.top = new_node
    else:
      new_node.next = self.top
      self.top = new_node

  def pop(self):
    """
    Returns value of node at top of stack, removes node from stack, and reassigns top of stack to next node.
    If stack is empty, raises an exception.
    """

    try:
      popped_node = self.top
      if popped_node.value == None:
        raise Exception('Stack is empty')
    except:
      print('Stack is empty')



### --------------- QUEUE CLASS CODE --------------- ###

class Queue:

  def __init__(self, front=None, back=None):
    """
    Creates a queue instance with empty "front" and "back" values
    """
    self.front = front
    self.back = back