# import pytest
# from code_challenges.linked_list.linked_list import LinkedList, Node

# pytestmark = [pytest.mark.version_1]

# ### These are my tests from following along in the lecture ###

# def test_node_instance():
#     node = Node('apples', None)
#     actual = node.value
#     expected = 'apples'
#     assert actual == expected
#     assert node.next == None

# def test_two_nodes():
#     node2 = Node('orange', None)
#     node1 = Node('apples', node2)

#     actual = node1.next.value
#     expected = 'orange'
#     assert actual == expected


# ### --------------------------------- ###

# # test 1: instantiate an empty linked list
# @pytest.mark.skip("pending")
# def test_one():
#     ll = LinkedList()
#     assert ll

# # test 2: insert into linked list
# @pytest.mark.skip("pending")
# def test_two():
#     ll = LinkedList()
#     ll.insert('apples')
#     actual = ll.head.value
#     expected = 'apples'
#     assert actual == expected

# # test 3: The head property will properly point to the first node in the linked list
# @pytest.mark.skip("pending")
# def test_three():
#     ll = LinkedList()
#     ll.insert('a')
#     ll.insert('b')
#     ll.insert('c')
#     actual = ll.head.value
#     expected = 'c'
#     assert actual == expected

# # test 4: Can properly insert multiple nodes into the linked list
# # def test_four():

# # test 5: Will return true when finding a value within the linked list that exists
# @pytest.mark.skip("pending")
# def test_five():
#     ll = LinkedList(Node('apples', Node('oranges', Node('bananas', Node('grapes')))))
#     actual_grapes = ll.includes('grapes')
#     expected_grapes = True
#     assert actual_grapes == expected_grapes


# # test 6: Will return false when searching for a value in the linked list that doesn't exist
# @pytest.mark.skip("pending")
# def test_six():
#     ll = LinkedList(Node('apples', Node('oranges', Node('bananas', Node('grapes')))))
#     actual = ll.includes('papaya')
#     expected = False
#     assert actual == expected

# # test 7: Can properly return a collection of all the values that exist in the linked list
# # def test_seven():

# # ---- Collaboration with Garfield Grant for help on Tests ----

# # def test_append_to_end():
# #     new_list = LinkedList(Node('1',Node('3',Node('2'))))
# #     new_list.append('5')
# #     actual= new_list.__str__()
# #     expected = "{'1'} ->{'3'} ->{'2'} ->{'5'} -> None "
# #     assert actual == expected

# # def test_insert_before_value():
# #     new_list = LinkedList(Node('1',Node('3',Node('2'))))
# #     new_list.insert_before_value('3','5')
# #     actual = new_list.__str__()
# #     expected = "{'1'} ->{'5'} ->{'3'} ->{'2'} -> None "
# #     assert actual == expected

# # def test_insert_after_value():
# #     new_list = LinkedList(Node('1',Node('3',Node('2'))))
# #     new_list.insert_after_value('3','5')
# #     actual = new_list.__str__()
# #     expected = "{'1'} ->{'3'} ->{'5'} ->{'2'} -> None "
# #     assert actual == expected


# # ---------- TESTS FOR CODE CHALLENGE 07 -------------

# def test_k_greater_than_length_of_ll():
#     ll = LinkedList(Node(1, Node(2, Node(3, Node(4, Node(5))))))
#     actual = ll.kthFromEnd(0)
#     expected = 5
#     assert actual == expected

# def test_k_equals_length_of_list():
#     ll = LinkedList(Node(1, Node(2, Node(3, Node(4, Node(5))))))
#     actual = ll.kthFromEnd(5)
#     expected = 'Same length'
#     assert actual == expected

# def test_k_is_not_positive_int():
#     ll = LinkedList(Node(1, Node(2, Node(3, Node(4, Node(5))))))
#     actual = ll.kthFromEnd(-1)
#     expected = 'Negative numbers not allowed'
#     assert actual == expected

# def test_list_is_size_of_one():
#     ll = LinkedList(Node(1))
#     actual = ll.kthFromEnd(0)
#     expected = 1
#     assert actual == expected

# def test_happy_path():
#     ll = LinkedList(Node(1, Node(2, Node(3, Node(4, Node(5))))))
#     actual = ll.kthFromEnd(3)
#     expected = 2
#     assert actual == expected
