from doubly_linked_list import ListNode,DoublyLinkedList
from collections import OrderedDict

class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        try:
            value = self.cache.pop(key)  #maintains caching order of ordered dictionary
            # print('val', value)
            self.cache[key] = value  
            # print('self.cache[key]', self.cache[key])
            return value
        except:
            print('key not found in cache')

    def set(self,key,value):
        if len(self.cache) >= self.capacity:
            # print('reached capacity of cache')
            #evict the lru.  delete the oldest key/val in cache
            if key in self.cache:
                self.cache.pop(key)
                self.cache[key] = value
            else:
                lru = list(self.cache.items())[0][0]
                lru_val = self.cache.pop(lru)
                print('lru_val',lru_val)
                #set new key/val to cache
                print('new key', key, 'new_val', value)
                self.cache[key] = value
        else:
            # value = self.cache.pop(key)
            self.cache[key] = value

    def print(self):
        for key in self.cache:
            print('key:', key, 'value:', self.cache[key])

# lru = LRUCache(3)

# lru.set('item1', 'a')
# lru.set('item2', 'b')
# lru.set('item3', 'c')

# lru.set('item2', 'z')

# lru.set('item-x', 'x')

# # lru.print()
# # print(lru.get('item2'))

# lru.print()







