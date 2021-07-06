# Stacks and Queues
<!-- Short summary or background information -->

## Challenge

**Challenge Type**: New implementation

Using a `Linked List` as the underlying data storage mechanism, implement both a **`stack`** and a **`queue`**

### Features

**Node**:

* [ ] Create a `Node` class that has properties for the *value* stored in the `Node`, and a pointer to the next `Node`

**Stack**:

* [ ] Create a `Stack` class that has a `top` property. It creates an empty `Stack` when instantiated.

  * [ ] This object should be aware of a default *empty value* assigned to `top` when the `stack` is created
  * [ ] The class should contain the following methods:
    * [ ] Push
      * Arguments: *value*
      * Adds a new `node` with that value to the `top` of the `stack` with an O(1) Time performance
    * [ ] Pop
      * Arguments: *none*
      * Returns: the value from `node` from the top of the `stack`
      * Removes the `node` from the `top` of the `stack`
      * Should raise exception when called on empty `stack`
    * [ ] Peek
      * Arguments: *none*
      * Returns: *Value* of the `node` located at the `top` of the `stack`
      * Should raise exception when called on empty `stack`
    * [ ] isEmpty
      * Arguments: *none*
      * Returns: Boolean indicating whether or not the `stack` is empty

**Queue**:

* [ ] Create a `Queue` class that has a `front` property. It creates an empty `Queue` when instantiated.
  * [ ] This object should be aware of a default *empty value* assigned to `front` when the `queue` is created
  * [ ] The class should contain the following methods:
    * [ ] Enqueue
      * Arguments: *value*
      * adds a new `node` with that value to `back` of the queue with an O(1) Time performance
    * [ ] Dequeue
      * [ ] Arguments: *none*
      * [ ] Returns: the *value* from `node` from the `front` of the `queue`
      * [ ] Removes the `node` from the `front` of the queue
      * [ ] Should raise exception when called on empty `queue`
    * [ ] Peek
      * [ ] Arguments: *none*
      * [ ] Returns: *Value* of the `node` located at the `front` of the `queue`
      * Should raise exception when called on empty `queue`
    * [ ] isEmpty
      * [ ] Arguments: *none*
      * [ ] Returns: Boolean indicating whether or not the `queue` is empty

You have access to the `Node class` and all the properties on the `Linked List class`.

## Approach & Efficiency

### Structure & Testing

Write tests to prove the following functionality:

1. [ ] Can successfully push onto a stack
2. [ ] Can successfully push multiple values onto a stack
3. [ ] Can successfully pop off the stack
4. [ ] Can successfully empty a stack after multiple pops
5. [ ] Can successfully peek the next item on the stack
6. [ ] Can successfully instantiate an empty stack
7. [ ] Calling pop or peek on empty stack raises exception
8. [ ] Can successfully enqueue into a queue
9. [ ] Can successfully enqueue multiple values into a queue
10. [ ] Can sucessfully dequeue out of a queue the expected value
11. [ ] Can successfully peek into a queue, seeing the expected value
12. [ ] Can successfully empty a queue after multiple dequeues
13. [ ] Can successfully instantiate an empty queue
14. [ ] Calling dequeue or peek on empty queue raises exception

## API
<!-- Description of each method publicly available to your Stack and Queue-->