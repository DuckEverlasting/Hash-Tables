# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return self._hash_djb2(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash = 5381
        for i in key:
            hash = (hash * 33) + ord(i)
        return hash


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.
        '''
        mod = self._hash_mod(key)
        node = self.storage[mod]
        if node is None:
            self.storage[mod] = LinkedPair(key, value)
        elif node.key is key:
            node.value = value
        else:
            while node.next is not None:
                if node.next.key is key:
                    node.next.value = value
                node = node.next
            node.next = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.
        '''
        mod = self._hash_mod(key)
        node = self.storage[mod] 
        if node is not None:
            if node.key is key:
                self.storage[mod] = node.next    
                return
            else:
                while node.next is not None:
                    prev = node
                    node = node.next
                    if node.key is key:
                        prev.next = node.next
                        return
        print("KEY NOT FOUND")
        


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.
        '''
        mod = self._hash_mod(key)
        node = self.storage[mod] 
        if node is not None:
            if node.key is key:
                return node.value
            else:
                while node.next is not None:
                    node = node.next
                    if node.key is key:
                        return node.value
        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        '''
        self.capacity *= 2
        prev_storage = self.storage
        self.storage = [None] * self.capacity
        for i in prev_storage:
            while i is not None:
                if i.next is not None:
                    curr = i.next
                    prev = i
                    while curr.next is not None:
                        prev = curr
                        curr = curr.next
                    self.insert(curr.key, curr.value)
                    prev.next = None
                else:
                    self.insert(i.key, i.value)
                    i = None
                



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
