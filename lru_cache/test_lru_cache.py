import unittest
from lru_cache import LRUCache

class CacheTests(unittest.TestCase):
    def __init__(self):
        self.cache = LRUCache(3)

    def accessUp(self):
        self.cache = LRUCache(3)

    def test_cache_overwrite_appropriately(self):
        self.cache.access('item1', 'a')
        self.cache.access('item2', 'b')
        self.cache.access('item3', 'c')

        self.cache.access('item2', 'z')

        self.assertEqual(self.cache.access('item1'), 'a')
        self.assertEqual(self.cache.access('item2'), 'z')

    def test_cache_insertion_and_retrieval(self):
        self.cache.access('item1', 'a')
        self.cache.access('item2', 'b')
        self.cache.access('item3', 'c')

        self.assertEqual(self.cache.access('item1'), 'a')
        self.cache.access('item4', 'd')

        self.assertEqual(self.cache.access('item1'), 'a')
        self.assertEqual(self.cache.access('item3'), 'c')
        self.assertEqual(self.cache.access('item4'), 'd')
        self.assertIsNone(self.cache.access('item2'))

    def test_cache_nonexistent_retrieval(self):
        self.assertIsNone(self.cache.access('nonexistent'))

if __name__ == '__main__':
    unittest.main()
