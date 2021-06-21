class Node:
    """
    Node class
    """

    def __init__(self, value, next=None):
        """
        Creates a Node instance
        """
        self.value = value
        self.next = next

    def __str__(self):
        """
        Prints data of the Node
        """
        return str(self.value)

class LinkedList:
    """
    Linked List class
    """

    def __init__(self, head=None):
        """
        Creates an instance of a Linked List
        """

        self.head = head

    def __str__(self):
        """
        Prints data of the Linked List
        """

        list_values = []
        if self.head is None:
            return "There is no node"

        current = self.head
        # print(current.__str__())

        while current is not None:
            list_values.append(current.value)
            current = current.next

        print("this is list", list_values)


    def insert(self, value):
        """
        Function inserts a Node with the value into the front of the Linked List
        """
        node = Node(value)

        if self.head is not None:
            node.next = self.head
        self.head = node

    def includes(self, value):
        """
        Searches the Linked List for the specified value
        """
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False



# ------------------------------------------------------------ #

if __name__ == "__main__":

#     ll = LinkedList()
#     node1 = Node('apples', None)
#     node2 = Node('oranges', None)
#     node3 = Node('pears', None)

#     ll.head == node1
#     node1.next == node2
#     node2.next == node3

#     ll.insert(node1)

#     print(ll.__str__())
#     print(ll.head.value)

# # llhead = 'apples' -> 'oranges' -> 'pear' -> None

    node1 = Node('apples')
    node2 = Node('bananas', node1)
    node3 = Node('cherries', node2)
    # print(node1.__str__())

    ll = LinkedList(node1)
    ll.insert(node2)
    ll.insert(node3)

    print(ll.__str__())
