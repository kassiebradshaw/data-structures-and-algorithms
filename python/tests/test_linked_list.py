from code_challenges.linked_list.linked_list import LinkedList, Node

### These are my tests from following along in the lecture ###

def test_node_instance():
    node = Node('apples', None)
    actual = node.value
    expected = 'apples'
    assert actual == expected
    assert node.next == None

def test_two_nodes():
    node2 = Node('orange', None)
    node1 = Node('apples', node2)

    actual = node1.next.value
    expected = 'orange'
    assert actual == expected


### --------------------------------- ###

# test 1: instantiate an empty linked list
def test_one():
    ll = LinkedList()
    assert ll

# test 2: insert into linked list
def test_two():
    ll = LinkedList()
    ll.insert('apples')
    actual = ll.head.value
    expected = 'apples'
    assert actual == expected

# test 3: The head property will properly point to the first node in the linked list
def test_three():
    ll = LinkedList()
    ll.insert('a')
    ll.insert('b')
    ll.insert('c')
    actual = ll.head.value
    expected = 'c'
    assert actual == expected

# test 4: Can properly insert multiple nodes into the linked list
# def test_four():

# test 5: Will return true when finding a value within the linked list that exists
def test_five():
    ll = LinkedList(Node('apples', Node('oranges', Node('bananas', Node('grapes')))))
    actual_grapes = ll.includes('grapes')
    expected_grapes = True
    assert actual_grapes == expected_grapes


# test 6: Will return false when searching for a value in the linked list that doesn't exist
def test_six():
    ll = LinkedList(Node('apples', Node('oranges', Node('bananas', Node('grapes')))))
    actual = ll.includes('papaya')
    expected = False
    assert actual == expected

# test 7: Can properly return a collection of all the values that exist in the linked list
# def test_seven():
