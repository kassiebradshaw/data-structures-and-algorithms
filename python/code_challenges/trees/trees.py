from code_challenges.stack_and_queue.stack_and_queue import Queue, Node

class BTNode:

  def __init__(self, value, left=None, right=None):
    """Creates a node instance with a value, a left and a right"""

    self.value = value
    self.left = left
    self.right = right

# -----------------------------------------------#
  
class BinaryTree:
  
  def __init__(self, root=None):
    """Creates an instance of a Binary Tree with a root node"""
    self.root = root

# --- depth-first traversal methods --- #

  def preOrder(self):
    """ Traverses the Binary Tree in order of root >> left >> right 
    Returns an array of the values, ordered appropriately """
    # input <-- root node
    # output <-- pre-order output of tree node's values

    if self.root is None:
      return "Tree is empty"

    order = []

    def traverse(root):
      order.append(root.value)

      if root.left is not None:
        traverse(root.left)
      
      if root.right is not None:
        traverse(root.right)
      
    traverse(self.root)
    
    return order

# ------------------------------------- #

  def inOrder(self):
    """ Traverses the Binary Tree in order of left >> root >> right
    Returns an array of the values, ordered appropriately """
    # input <-- root node
    # output <-- in-order output of tree node's values

    if self.root is None:
      return "Tree is empty"
    
    order = []

    def traverse(root):
      if root.left is not None:
        traverse(root.left)
      
      order.append(root.value)
      
      if root.right is not None:
        traverse(root.right)
    
    traverse(self.root)

    return order

# ------------------------------------- #

  def postOrder(self):
    """ Traverses the Binary Tree in order of left >> right >> root
    Returns an array of the values, ordered appropriately """
    # input <-- root node
    # output <-- post-order output of tree node's values
    
    if self.root is None:
      return "Tree is empty"
    
    order = []

    def traverse(root):
      if root.left is not None:
        traverse(root.left)

      if root.right is not None:
        traverse(root.right)

      order.append(root.value)

    traverse(self.root)

    return order

# --- breadth-first traversal method --- #

  def breadth_first(self):
    """ Traverses the Binary Tree breadth-first """
    # input <-- root node
    # output <-- breadth-first output of tree node's values
    root = self.root

    if root is None:
      return "Tree is empty"

    else:
      order = []
      queue = Queue()
      queue.enqueue(root)

      while not queue.isEmpty():
        front = queue.dequeue()
        order.append(front.value)
        if front.left:
          queue.enqueue(front.left)
        if front.right:
          queue.enqueue(front.right)
      
    return order

# -----------------------------------------------#

  def max_value(self):

    if self.root is None:
      return "Tree is empty"
    
    value_list = self.preOrder()
    max_val = value_list[0]

    for i in value_list:
      if i > max_val:
        max_val = i
    
    return max_val

# -----------------------------------------------#

class BinarySearchTree(BinaryTree):
  """ Sub-class of the Binary Tree class """
  
  def __init__(self, root=None):
    """Creates an instance of a Binary Search Tree"""
    self.root = root

# ------------------------------------- #
  
  def add(self, value):
    """ Adds a node of the specified value to the BST"""

    if value is None or type(value) == str:
      return "Node must contain a number"
        
    new_node = BTNode(value)

    if self.root is None:
      self.root = new_node
      
    current = self.root

    while current:

      if current.value > value:
        if current.left is None:
          current.left = new_node
        else:
          current = current.left

      if current.value < value:
        if current.right is None:
          current.right = new_node
        else:
          current = current.right

      if current.value == value:
        return "Value is already in the tree"

# ------------------------------------- #

  def contains(self, value):
    """ Returns a Boolean verifying if BST contains a node of the specified value """
    
    current = self.root

    while current is not None:
      if current.value > value:
        current = current.left
      if current.value < value:
        current = current.right
      if current.value == value:
        return True
      else:
        return False
    
    # return False

    # --- Wondwosen's demo --- #

    # def contains(self, target):

    #   if self.root is None:
    #     return None

    #   current = self.root

    #   while current:
    #     if current.value == target:
    #       return True
    #     if target > current.value:
    #       current = current.right
    #     else:
    #       current = current.left
        
    #   return False

# --- Michael Hendricks' demo --- #

  # def contains(self, value):

  #   if self.root == value:
  #     return True
    
  #   if self.root > value:
  #     if self.left:
  #       return self.left.contains(value)
  #     else:
  #       return False
      
  #   else:
  #     if self.right:
  #       return self.right.contains(value)
  #     else:
  #       return False
    

