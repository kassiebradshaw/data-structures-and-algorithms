from code_challenges.stack_and_queue.stack_and_queue import Stack, CustomError

class PseudoQueue:
  def __init__(self):
    self.front = Stack() # "top" keeps track of front of queue
    self.rear = Stack() # "top" keeps track of rear of queue
  
  def enqueue(self, value):
    if self.front.isEmpty():
      self.front.push(value)
      self.rear.push(value)
  
  def dequeue(self):
    if len(self.stack2) == 0:
      if len(self.stack1) == 0:
        raise CustomError("Can't dequeue from an empty queue!")
      while len(self.stack1) > 0:
        current_stack1_item = self.stack1.pop()
        self.stack2.push(current_stack1_item)
    
    return self.stack2.pop()
