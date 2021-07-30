import pytest
from code_challenges.trees.trees import BTNode, BinaryTree, BinarySearchTree

# tests from 401 repo

def test_node_has_value():
  node = BTNode("apple")
  assert node.value == "apple"

def test_node_has_left_of_none():
  node = BTNode("apple")
  assert node.left is None

def test_node_has_right_of_none():
  node = BTNode("apple")
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

# --- TESTS FOR Code Challenge 16 --- #

def test_max_value(number_tree):
  actual = number_tree.max_value()
  expected = 80
  assert actual == expected

def test_max_value_incorrect(number_tree):
  actual = number_tree.max_value()
  expected = 75
  assert actual != expected

def test_example_tree_max_val(example_tree):
  actual = example_tree.max_value()
  expected = 11
  assert actual == expected

def test_empty_tree_max_val(empty_tree):
  actual = empty_tree.max_value()
  expected = "Tree is empty"
  assert actual == expected

def test_negative_tree_max_val(negative_tree):
  actual = negative_tree.max_value()
  expected = -2
  assert actual == expected

# --- TESTS FOR Code Challenge 17 --- #

def test_breadth_first_example_tree(example_tree):
  actual = example_tree.breadth_first()
  expected = [2,7,5,2,6,9,5,11,4]
  assert actual == expected

def test_breadth_first_negative_tree(negative_tree):
  actual = negative_tree.breadth_first()
  expected = [-2,-7,-5,-2,-6,-9, -5,-11,-4]
  assert actual == expected

def test_breadth_first_fruit_tree(fruit_tree):
  actual = fruit_tree.breadth_first()
  expected = ["Apple","Banana","Coconut","Date","Elderberry","Fig","Grape"]
  assert actual == expected

def test_breadth_first_number_tree(number_tree):
  actual = number_tree.breadth_first()
  expected = [50,25,75,15,30,60,80]
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
def number_tree():
  tree = BinaryTree()
  tree.root = BTNode(50)
  tree.root.left = BTNode(25)
  tree.root.left.left = BTNode(15)
  tree.root.left.right = BTNode(30)
  tree.root.right = BTNode(75)
  tree.root.right.left = BTNode(60)
  tree.root.right.right = BTNode(80)
  return tree

@pytest.fixture
def example_tree():
  # the tree we were given in the instructions
  tree = BinaryTree()
  tree.root = BTNode(2)
  tree.root.left = BTNode(7)
  tree.root.left.left = BTNode(2)
  tree.root.left.right = BTNode(6)
  tree.root.left.right.left = BTNode(5)
  tree.root.left.right.right = BTNode(11)
  tree.root.right = BTNode(5)
  tree.root.right.right = BTNode(9)
  tree.root.right.right.left = BTNode(4)
  return tree

@pytest.fixture
def negative_tree():
  # testing a tree with all negative numbers
  tree = BinaryTree()
  tree.root = BTNode(-2)
  tree.root.left = BTNode(-7)
  tree.root.left.left = BTNode(-2)
  tree.root.left.right = BTNode(-6)
  tree.root.left.right.left = BTNode(-5)
  tree.root.left.right.right = BTNode(-11)
  tree.root.right = BTNode(-5)
  tree.root.right.right = BTNode(-9)
  tree.root.right.right.left = BTNode(-4)
  return tree

@pytest.fixture
def fruit_tree():
  tree = BinaryTree()
  tree.root = BTNode("Apple")
  tree.root.left = BTNode("Banana")
  tree.root.left.left = BTNode("Date")
  tree.root.left.right = BTNode("Elderberry")
  tree.root.right = BTNode("Coconut")
  tree.root.right.left = BTNode("Fig")
  tree.root.right.right = BTNode("Grape")
  return tree
