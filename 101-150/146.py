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
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = dict()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
            self.add(node)
            return node.value
        else:
            return -1
    
    def remove(self, node):
        """
        :type node: Node
        :rtype: void
        """         
        previous = node.prev
        nextNode = node.next
        previous.next = nextNode
        nextNode.prev = previous
        
    def add(self, node):
        """
        :type node: Node
        :rtype void
        """
        previousNode = self.tail.prev
        previousNode.next = node
        node.prev = previousNode
        node.next = self.tail
        self.tail.prev = node

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        
        if key not in self.hashmap:
            self.hashmap[key] = Node(key, value)
            self.add(self.hashmap[key])
        else:
            #node to be removed
            node = self.hashmap[key]
            self.remove(node)
            del self.hashmap[node.key]
            
            #node to be added
            NodE = Node(key, value)
            self.add(NodE)
            self.hashmap[key] = NodE
            
        #capacity exceeded
        if len(self.hashmap) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.hashmap[node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
