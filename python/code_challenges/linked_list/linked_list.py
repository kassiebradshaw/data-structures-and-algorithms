class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        pass

    def some_method(self):
        # method body here
        pass

class Node:
    """
    Put docstring here
    """

    def __init__(self, value, next):
        self.value = value
        self.next = next


if __name__ == "__main__":
    ll = LinkedList()
    node1 = Node('apples', None)
    node2 = Node('oranges', None)
    node3 = Node('pears', None)

    ll.head == node1
    node1.next == node2
    node2.next == node3

    # llhead = 'apples' -> 'oranges' -> 'pear' -> None
