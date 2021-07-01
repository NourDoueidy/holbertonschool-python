#!/usr/bin/python3
''' MRU Cache '''

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    ''' defines a class '''

    def __init__(self):
        ''' initializer '''
        super().__init__()
        self.mru_order = OrderedDict()

    def put(self, key, item):
        ''' self descriprive '''
        if not key or not item:
            return

        self.cache_data[key] = item
        self.mru_order[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_discarded = next(iter(self.mru_order))
            del self.cahe_data[item_dicarded]
            print("DISCARD:", item_discarded)

        if len(self.mru_order) > BaseCaching.MAX_ITEMS:
            self.mru.popitem(last=False)

        self.mru_order.move_to_end(key, false)

    def get(self, key):
        ''' self descriptive '''
        if key in self.cache_data:
            self.mru_order.move_to_end(key, False)
            return self.cache_data[key]
        return None
