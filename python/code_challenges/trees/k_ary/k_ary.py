from ...stack_and_queue.stack_and_queue import Queue

class treeNode:

  def __init__(self, value):
    """Creates a node instance with a value, and an empty list to hold the child nodes"""

    self.value = value
    self.children = []

class k_ary:

  def __init__(self, root=None):
    """Creates an instance of a k-ary tree with a root node"""
    self.root = root