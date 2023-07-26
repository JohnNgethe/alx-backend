#!/usr/bin/env python3
"""
    3-lru_cache mod
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
        implementation of the Least Recently Used
        cache replacement policy
    """
    def __init__(self):
        """ constructor function """
        self.__cache_checker = []
        super().__init__()

    def put(self, key, item):
        """
            sets the given key to the item in the caching
            system
        """
        if key is None or item is None:
            return

        if len(self.cache_data) != BaseCaching.MAX_ITEMS:
            self.cache_data[key] = item
            self.__cache_checker.append(key)
        else:
            # key is present no need for replacement
            if self.cache_data.get(key):
                return
            discarded = self.__cache_checker.pop(0)
            print("DISCARD: {}".format(discarded))
            del self.cache_data[discarded]

            self.cache_data[key] = item
            self.__cache_checker.append(key)

    def get(self, key):
        """
            gets the item at the given key in the caching
            system
        """
        if key is None or not self.cache_data.get(key):
            return None

        self.__cache_checker.pop(self.__cache_checker.index(key))
        self.__cache_checker.append(key)
        return self.cache_data.get(key)
