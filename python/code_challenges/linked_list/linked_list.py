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

        string = ""

        current = self.head

        while current is not None:
            string += f"{ {current.value} } -> "
            current = current.next

        string += f" None "

        return string


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

    def append(self, value):
        current = self.head
        newNode = Node(value)

        if current is None:
            self.head = newNode

        while current is not None:
            if current.next == None:
                current.next = newNode
            else:
                current = current.next


    def insertAfter(self, value, newValue):
        current = self.head
        newNode = Node(newValue)

        if current is None:
            self.head = newNode
        while current is not None:
            if current == value:
                current.next == newNode
            else:
                current = current.next

    def insertBefore(self, value, newValue):
        current = self.head
        newNode = Node(newValue)

        if current is None:
            self.head = newNode
        while current is not None:
            if current.next == value:
                current = newNode
            else:
                current = current.next

    # https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/
    def kthFromEnd(self, k):
        temp = self.head
        length = 0

        while temp is not None:
            temp = temp.next
            length += 1

        #print count
        if k > length: # if entered location is greater than length of LL
            return 'Location is greater than the length of LL'
        if k == length:
            return 'Same length'
        if k < 0:
            return 'Negative numbers not allowed'


        temp = self.head
        for i in range(1, length - k):
            temp = temp.next

        return temp.value


list1 = LinkedList('1', Node('3', Node('5')))
list2 = LinkedList('2', Node('4', Node('6')))

def zipLists(list1, list2):
    list1_current = list1.head # 1
    list2_current = list2.head # 2

    while list1_current and list2_current != None: # while 1 and 2 are not none
        list1_next = list1_current.next # 1's next = 3
        list2_next = list2_current.next # 2's next = 4

        list1_current.next = list2_current # 1's next = 2
        list2_current.next = list1_next # 2's next = 3

        list1_current = list1_current.next
        list2_current = list2_current.next


# --------------Garfield helped

    # def __str__(self):
    #     string_value = ""
    #     current = self.head
    #     while current is not None:
    #         string_value += f"{ {current.value} } ->"
    #         current = current.next
    #     string_value += f" None "
    #     return string_value



# ------------------------------------------------------------ #

# if __name__ == "__main__":

# #     ll = LinkedList()
# #     node1 = Node('apples', None)
# #     node2 = Node('oranges', None)
# #     node3 = Node('pears', None)

# #     ll.head == node1
# #     node1.next == node2
# #     node2.next == node3

# #     ll.insert(node1)

# #     print(ll.__str__())
# #     print(ll.head.value)

# # # llhead = 'apples' -> 'oranges' -> 'pear' -> None

#     node1 = Node('apples')
#     node2 = Node('bananas', node1)
#     node3 = Node('cherries', node2)
#     # print(node1.__str__())

#     ll = LinkedList(node1)
#     ll.insert(node2)
#     ll.insert(node3)

#     print(ll.__str__())
