from doubly_linked_list import DoublyLinkedList

# def set(self, key, value):
#     pass
#     if self.record.length == self.limit:
#         old_key = self.record.remove_from_tail()
#         if key not in self.storage.keys():
#             del self.storage[old_key] # deletes key 
#         self.record.add_to_head(key)
#         self.storage[key] = (value, self.record.head)
#     else:
#         self.record.add_to_head(key)
#         self.storage[key] =(value, self.record.head)


class RingBuffer:
    #the ring buffer is very similar to our LRUCache 
    #append adds elements to the buffer 
    #if element at max capacity overwrite oldest element in buffer 
    #oldest element in buffer is oldest one (the one that was first added and so on)
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity: 
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        
        if self.storage.length == self.capacity: 
            self.current.value = item 
            if self.current is self.storage.tail:
                self.current = self.storage.head
            else: 
                self.current = self.current.next

    def get(self):
        #get returns our elements in our DLLl
        #even if there are none elements in our DLL don't return them 

        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head 
        while current: 
            list_buffer_contents.append(current.value)
            current = current.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
