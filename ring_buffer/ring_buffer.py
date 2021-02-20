from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity=0):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # before reaching capacity, keep track of most recent added item and add new item to tail
        if self.storage.len() < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        # do the following when the list becomes full
        elif self.storage.len() == self.capacity:
            if self.current.next == None:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head
            else:
                self.current.next.delete()
                self.current.insert_after(item)
                self.current = self.current.next

    def get(self):
        buffer = []
        curr_item = self.storage.head

        if curr_item is not None:
            while curr_item.next is not None:
                buffer.append(curr_item.value)
                curr_item = curr_item.next
            buffer.append(curr_item.value)

        return buffer
