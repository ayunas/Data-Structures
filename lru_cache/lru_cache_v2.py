from doubly_linked_list import ListNode,DoublyLinkedList
from collections import OrderedDict


class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        try:
            value = self.cache.pop(key)  #maintains caching order of ordered dictionary
            self.cache[key] = value  
            return value
        except:
            print('key not found in cache')

    def set(self,key,value):
        if len(self.cache) >= self.capacity:
            print('reached capacity of cache')
            #evict the lru.  delete the oldest key/val in cache
            first = list(self.cache.items())[0][0]
            self.cache.pop(first)
            #set new key/val to cache
            self.cache[key] = value

    def print(self):
        for key in self.cache:
            print('key:', key, 'value:', self.cache[key])

lru = LRUCache(3)
lru.cache['one'] = 1
lru.cache['two'] = 2
lru.cache['three'] = 3
lru.cache['four'] = 4
# lru.print()

# lru.get('two')
lru.set('eight',8)
lru.print()





