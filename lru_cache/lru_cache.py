import random
from doubly_linked_list import ListNode,DoublyLinkedList

# node = ListNode(3)
# node.insert_after(30)
# ll = DoublyLinkedList(node)
# ll.add_to_tail(50)
# ll.add_to_tail(75)
# ll.add_to_head(20)
# ll.display()

# cache hit / cache miss
# LRU = tail of doubly linked list
# remove item from linked list and hash map
# set up linked list with the most-recently used item at the head of the list and the least-recently used item at the tail:

class Cache:
    def __init__(self,newest,oldest):
        self.MRU = ListNode(newest)
        self.LRU = oldest
        self.list = DoublyLinkedList(self.MRU)
        # self.list.add_to_head(newest)  #add to head takes an int. DLL() takes in a node
        self.list.add_to_tail(oldest)
        self.hashmap = {}

    def displaylist(self):
        n = self.list.head
        while n != None:
            print(n.value)
            n = n.next
    
    def get_node_value(self, search):
        n = self.list.head
        while n != None:
            if n.value == search:
                print('found node value', n.value)
                return n.value
            elif n.next == None:
                print('no node value found')
                return None
            n = n.next
        
    
    def printhashmap(self):
        for key in self.hashmap:
            print('key', key, 'value', self.hashmap[key])

    def access(self,node):
        print('hashmap len', len(self.hashmap))
        # print(list(self.hashmap.values()))

        if node in self.hashmap:
            cache_hit = self.hashmap[node]
            print('cache_hit', cache_hit)
        else:
            if len(self.hashmap >= 5):
                pass
            else:
                self.hashmap[node] = node.value
                cache_miss = self.hashmap[node]
                print('cache_miss.set the node to MRU and in the cache')

    def evict(self):
        pass

    def add_node(self,val):
        self.list.add_to_tail(val)


cache = Cache(100,20)
cache.add_node(40)
cache.displaylist()
cache.get_node_value(400)
# cache.access(20)







# class LRUCache:
#     """
#     Our LRUCache class keeps track of the max number of nodes it
#     can hold, the current number of nodes it is holding, a doubly-
#     linked list that holds the key-value entries in the correct
#     order, as well as a storage dict that provides fast access
#     to every node stored in the cache.
#     """
#     def __init__(self, limit=10):
#         pass

#     """
#     Retrieves the value associated with the given key. Also
#     needs to move the key-value pair to the end of the order
#     such that the pair is considered most-recently used.
#     Returns the value associated with the key or None if the
#     key-value pair doesn't exist in the cache.
#     """
#     def get(self, key):
#         pass

#     """
#     Adds the given key-value pair to the cache. The newly-
#     added pair should be considered the most-recently used
#     entry in the cache. If the cache is already at max capacity
#     before this entry is added, then the oldest entry in the
#     cache needs to be removed to make room. Additionally, in the
#     case that the key already exists in the cache, we simply
#     want to overwrite the old value associated with the key with
#     the newly-specified value.
#     """
#     def set(self, key, value):
#         pass
