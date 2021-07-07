# Stacks and Queues

## Challenge Type: New Implementation

Using a `Linked List` as the underlying data storage mechanism, implement both a **`stack`** and a **`queue`**

[Link to Pull Request](https://github.com/kassiebradshaw/data-structures-and-algorithms/pull/31)

---

### Features

* [x] Create a `Node` class that has properties for the *value* stored in the `Node`, and a pointer to the next `Node`

* [x] Create a `Stack` class that has a `top` property. It creates an empty `Stack` when instantiated.

  * [x] This object should be aware of a default *empty value* assigned to `top` when the `stack` is created
  * [x] The class should contain the following methods:
    * [x] Push
    * [x] Pop
    * [x] Peek
    * [x] isEmpty

* [x] Create a `Queue` class that has a `front` property. It creates an empty `Queue` when instantiated.
  * [x] This object should be aware of a default *empty value* assigned to `front` when the `queue` is created
  * [x] The class should contain the following methods:
    * [x] Enqueue
    * [x] Dequeue
    * [x] Peek
    * [x] isEmpty

You have access to the `Node class` and all the properties on the `Linked List class`.

---

## Approach & Efficiency

---

## Structure & Testing

Write tests to prove the following functionality:

1. [x] Can successfully push onto a stack
2. [x] Can successfully push multiple values onto a stack
3. [x] Can successfully pop off the stack
4. [x] Can successfully empty a stack after multiple pops
5. [x] Can successfully peek the next item on the stack
6. [x] Can successfully instantiate an empty stack
7. [x] Calling pop or peek on empty stack raises exception
8. [x] Can successfully enqueue into a queue
9. [x] Can successfully enqueue multiple values into a queue
10. [x] Can successfully dequeue out of a queue the expected value
11. [x] Can successfully peek into a queue, seeing the expected value
12. [x] Can successfully empty a queue after multiple dequeues
13. [x] Can successfully instantiate an empty queue
14. [x] Calling dequeue or peek on empty queue raises exception

---

## API
<!-- Description of each method publicly available to your Stack and Queue-->
### Stack Methods

* `.push(value)`
  * Arguments: *value*
  * Adds a new node with that value to the top of the stack with an O(1) Time performance

* `.pop()`
  * Arguments: *none*
    * Returns: the value from node from the top of the stack
    * Removes the node from the top of the stack
    * Should raise exception when called on empty stack

* `.peek()`
  * Arguments: *none*
  * Returns: *Value* of the node located at the top of the stack
  * Should raise an exception when called on an empty stack

* `.isEmpty()`
  * Arguments: *none*
  * Returns: Boolean indicating whether or not the stack is empty

### Queue Methods

* `.enqueue(value)`
  * Arguments: *value*
  * Adds a new node with that value to the back of the queue with an O(1) Time performance

* `.dequeue()`
  * Arguments: *none*
  * Returns: the *value* of the node from the front of the queue
  * Removes the node from the front of the queue
  * Should raise an exception when called on an empty queue

* `.peek()`
  * Arguments: *none*
  * Returns: the *value* of the node located at the front of the queue
  * Should raise an exception when called on an empty queue

* `.isEmpty()`
  * Arguments: *none*
  * Returns: Boolean indicating whether or not the queue is empty

## Collaboration & Credit

* Thanks Ben Hill for help with raising/testing exceptions!
* Thanks Anthony Beaver for help making a fixture!
