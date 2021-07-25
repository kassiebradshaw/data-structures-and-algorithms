import pytest
from code_challenges.trees.trees import Node, BinaryTree, BinarySearchTree

# tests from 401 repo

def test_node_has_value():
  node = Node("apple")
  assert node.value == "apple"

def test_node_has_left_of_none():
  node = Node("apple")
  assert node.left is None

def test_node_has_right_of_none():
  node = Node("apple")
  assert node.right is None

def test_create_binary_tree():
  tree = BinaryTree()
  assert tree

def test_binary_tree_has_root():
  tree = BinaryTree()
  assert tree.root is None

def test_binary_tree_root(fruit_tree):
  actual = fruit_tree.root.value
  expected = "Apple"
  assert actual == expected

def test_create_binary_search_tree():
  tree = BinarySearchTree()
  assert tree

# --- My BinaryTree tests --- #

def test_pre_order_on_empty_tree(empty_tree):
  actual = empty_tree.preOrder()
  expected = "Tree is empty"
  assert actual == expected

def test_in_order_on_empty_tree(empty_tree):
  actual = empty_tree.inOrder()
  expected = "Tree is empty"
  assert actual == expected

def test_post_order_on_empty_tree(empty_tree):
  actual = empty_tree.postOrder()
  expected = "Tree is empty"
  assert actual == expected

def test_pre_order(fruit_tree):
  actual = fruit_tree.preOrder()
  expected = ["Apple", "Banana", "Date", "Elderberry", "Coconut", "Fig", "Grape"]
  assert actual == expected

def test_in_order(fruit_tree):
  actual = fruit_tree.inOrder()
  expected = ["Date", "Banana", "Elderberry", "Apple", "Fig", "Coconut", "Grape"]
  assert actual == expected

def test_post_order(fruit_tree):
  actual = fruit_tree.postOrder()
  expected = ["Date", "Elderberry", "Banana", "Fig", "Grape", "Coconut", "Apple"]
  assert actual == expected

# --- My Binary Search Tree Tests --- #

def test_add_node_to_empty_BST():
  tree = BinarySearchTree()
  tree.add(5)
  actual = tree.root.value
  expected = 5
  assert actual == expected

def test_add_non_int_node_to_BST():
  tree = BinarySearchTree()
  actual = tree.add("Hello")
  expected = "Node must contain a number"
  assert actual == expected

def test_add_empty_node_to_BST():
  tree = BinarySearchTree()
  actual = tree.add("")
  expected = "Node must contain a number"
  assert actual == expected

def test_add_node_to_non_empty_BST():
  tree = BinarySearchTree()
  tree.add(5)
  tree.add(10)
  actual = tree.root.right.value
  expected = 10
  assert actual == expected

def test_add_node_again():
  tree = BinarySearchTree()
  tree.add(5)
  tree.add(10)
  tree.add(7)
  actual = tree.root.right.left.value
  expected = 7
  assert actual == expected

def test_contains_method_returns_false():
  tree = BinarySearchTree()
  tree.add(5)
  tree.add(6)
  tree.add(7)
  tree.add(8)
  actual = tree.contains(9)
  expected = False
  assert actual == expected

# --- Fixtures --- #

@pytest.fixture
def empty_tree():
  empty_tree = BinaryTree()
  return empty_tree

@pytest.fixture
def fruit_tree():
  tree = BinaryTree()
  tree.root = Node("Apple")
  tree.root.left = Node("Banana")
  tree.root.left.left = Node("Date")
  tree.root.left.right = Node("Elderberry")
  tree.root.right = Node("Coconut")
  tree.root.right.left = Node("Fig")
  tree.root.right.right = Node("Grape")
  return tree
