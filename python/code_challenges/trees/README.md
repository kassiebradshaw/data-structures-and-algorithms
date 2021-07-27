# Code Challenge 15 - Binary Tree and BST Implementation

## Challenge Type: New Implementation

[Link to Code](trees.py)

[Link to Pull Request](https://github.com/kassiebradshaw/data-structures-and-algorithms/pull/35)

---

## Features

**Node**:

* [x] Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

**Binary Tree**:

* [x] Create a Binary Tree class
  * [x] Define a method for each of the depth-first traversals:
    * [x] Pre-order
    * [x] In-order
    * [x] Post-order (which returns an array of the values, ordered appropriately)
* [x] Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

**Binary Search Tree**:

* [x] Create a Binary Search Tree class
  * [x] This class should be a sub-class of the Binary Tree Class, with the following additional methods:
    * [x] **Add** - adds a new node with that value in the correct location in the binary search tree
      * Arguments: value
      * Return: nothing
    * [x] **Contains**
      * Arguments: value
      * Returns: boolean indicating whether or not the value is in the tree at least once.

---

## Structure and Testing

Write tests to prove the following functionality:

* [x] Can successfully instantiate an empty tree
* [x] Can successfully instantiate a tree with a single root node
* [x] Can successfully add a left child and right child to a single root node
* [x] Can successfully return a collection from a preorder traversal
* [x] Can successfully return a collection from an inorder traversal
* [x] Can successfully return a collection from a postorder traversal

## Collaboration & Credit

* [Used the starter tests from the 401 class repo](https://github.com/codefellows/seattle-code-python-401n3/blob/main/class-15/demo/test_tree.py)

* Credit to Wondwosen and Michael Hendricks for their Binary Search Tree "contains" methods
