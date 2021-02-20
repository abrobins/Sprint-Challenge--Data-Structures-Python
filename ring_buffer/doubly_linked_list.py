"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
           # self.next.prev = self.prev

            # could also do this here instead of line above
            next_node = self.next
            next_node.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def len(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # create a new node
        # don't have to include None, None
        new_node = ListNode(value, None, None)
        # first check if the DLL is empty
        # if empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            # the list already has elements
            # make new node's next value point to current head
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):

        # artem's code
        # if self.head is None:
        #   return None
        # head_value = self.head.value
        # self.delete(self.head)
        # return head_value

        # we have a situation where head has a previous value so make sure to remove head same with remove_from_tail
        # check if dll is empty
        if not self.head and not self.tail:
            return None
        # check if dll has just 1 node
        if self.length == 1:
            # assign current head value
            h_value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return h_value
        # if more than 1 node, get the head
        h_value = self.head.value
        self.head.next.prev = None
        self.head = self.head.next
        self.length -= 1
        return h_value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        # check if dll is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # node is not empty need to add node to tail
        else:
            # insert new_node after current tail
            new_node.prev = self.tail
            self.tail.next = new_node
            # point tail to new_node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if self.tail is None:
            return None
        tail_value = self.tail.value
        # delete tail from dll
        self.delete(self.tail)
        return tail_value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is self.head:
            return None
        head_value = node.value
        self.delete(node)
        self.add_to_head(head_value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node is self.tail:
            return None
        end_value = node.value
        self.delete(node)
        self.add_to_tail(end_value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # look at Artem's code on this one
        # check if self.head is self.tail possibly
        self.length -= 1
        if node is self.head:
            self.head = node.next
        if node is self.tail:
            self.tail = node.prev
        node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        max = 0
        if self.length:
            current = self.head
            max = current.value
        while current.next:
            if current.next.value > max:
                max = current.next.value
            current = current.next
        return max
