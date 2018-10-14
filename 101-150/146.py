'''

146. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

'''

'''
Logic 
*** Use a dictionary with key : Node(key, value) pairs; where the Node(key, value) instances are objects of a doubly linked list structure. 
Maintain internal variable for capacity. Imagine the data structure as a key pointing to DLL objects where DLL objects are internally a chain of DLL structure which have external
incoming references from the dictionary. 

For get operation, if the node exists, return its value. As it was just accessed; remove it from wherever it is in the DLL structure; then add it again to the tail of the DLL. Why? -
we are trying to have a queue like FIFO structure where shuffling can be done in O(1). So we are hacking FIFO with out DLL implementation. If the tail.prev element is the most recently
accessed obj, then the head.next is the LRU object which will be flushed when capacity is reached.

For put operation, if the key exits -> just remove the respective node from DLL and dict; and add the key,value from args to refresh the usage of the key. 
The meat logic comes when the element doesn't exist. What do we do then? -> add the element to the dictionary and to the tail of the DLL; then check if the len(dictionary) is more 
than the desired capacity? - is it more? yes? -> then evict the head.next element as it has to be LRU element; also remove the element from the dictionary.***
'''

class Node:
    def __init__(self, key=None, val = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.tail, self.head = Node(None, None), Node(None, None)
        self.head.next, self.tail.prev = self.tail, self.head
        self.hash = dict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash:
            xnode = self.hash[key]
            self._remove(xnode)
            self._add(xnode)
            return xnode.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.hash:
            if self.capacity == len(self.hash):
                xnode = self.head.next
                self._remove(xnode)
                del self.hash[xnode.key]
        else:
            xnode = self.hash[key]
            self._remove(xnode)
            
        nNode = Node(key, value)
        self._add(nNode)
        self.hash[key] = nNode
            
        
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def _add(self, node):
        prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        node.prev = prev
        prev.next = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
