class LinkedList:
    """
    Creates a Linked List class
    """

    def __init__(self, head=None):
        """
        Creates an instance of a Linked List
        """
        self.head = head

    def __str__(s):
        pass

    def insert(self, value):
        """
        Function inserts a Node with the value into the Linked List
        """
        node = Node(value)

        if self.head is not None:
            node.next = self.head
        self.head = node

    def includes(self, value):
        """
        """
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False


class Node:
    """
    Creates a Node class
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# ------------------------------------------------------------ #

if __name__ == "__main__":
    ll = LinkedList()
    node1 = Node('apples', None)
    node2 = Node('oranges', None)
    node3 = Node('pears', None)

    ll.head == node1
    node1.next == node2
    node2.next == node3

    # llhead = 'apples' -> 'oranges' -> 'pear' -> None
