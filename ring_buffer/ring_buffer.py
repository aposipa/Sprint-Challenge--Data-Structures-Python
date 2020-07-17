from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity > self.storage.length:
            self.storage.add_to_tail(item)
            self.current = self.storage.head

        elif self.capacity == self.storage.length:
            delete_this = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            
            if delete_this == self.current:
                self.current = self.storage.tail

    def get(self):
        list_buffer_contents = []

        start_node = self.current
        list_buffer_contents.append(start_node.value)

        if start_node.next is not None:
            next = start_node.next
        else:
            next = self.storage.head
        while next != start_node:
            list_buffer_contents.append(next.value)
            if next.next is not None:
                next = next.next
            else:
                next = self.storage.head
        return list_buffer_contents