class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def add_front(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1

    def remove_last(self):
        node = self.tail.prev
        self.remove(node)
        return node

class LFUCache(object):

    def __init__(self, capacity):

        self.capacity = capacity
        self.size = 0
        self.min_freq = 0

        # key -> Node
        self.key_node = {}

        # frequency -> DoublyLinkedList
        self.freq_list = {}

    def increase_frequency(self, node):
        old_freq = node.freq

        # Remove from old frequency list
        self.freq_list[old_freq].remove(node)

        # If minimum frequency list becomes empty
        if old_freq == self.min_freq:
            if self.freq_list[old_freq].size == 0:
                self.min_freq += 1

        # Increase frequency
        node.freq += 1
        new_freq = node.freq

        # Create list if it doesn't exist
        if new_freq not in self.freq_list:
            self.freq_list[new_freq] = DoublyLinkedList()

        # Add to front because it is now most recently used
        self.freq_list[new_freq].add_front(node)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_node:
            return -1

        node = self.key_node[key]

        # Using the key increases its frequency
        self.increase_frequency(node)

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0:
            return

        # Key already exists
        if key in self.key_node:
            node = self.key_node[key]

            # Update value
            node.value = value

            # put also increases frequency
            self.increase_frequency(node)

            return

        # Cache is full
        if self.size == self.capacity:

            # Remove LFU key.
            # If frequency is tied, remove LRU key.
            node = self.freq_list[self.min_freq].remove_last()

            del self.key_node[node.key]

            self.size -= 1

        # Insert new key
        node = Node(key, value)

        # New key always starts with frequency 1
        self.min_freq = 1

        if 1 not in self.freq_list:
            self.freq_list[1] = DoublyLinkedList()

        self.freq_list[1].add_front(node)

        self.key_node[key] = node
        self.size += 1

