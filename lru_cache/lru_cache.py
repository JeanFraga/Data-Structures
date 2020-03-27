# import sys
# sys.path.append('../GitHub/Data-Structures/doubly_linked_list')
# from doubly_linked_list import ListNode
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        # self.node = ListNode(0)
        # self.dll = DoublyLinkedList(self.node)
        # self.size = 0
        self.dll = DoublyLinkedList()
        self.dict = dict()



    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # if self.dict.get(key) is None:
        #     return None

        if key not in self.dict:
            return None
        # if key in self.dict:
        # self.dll.move_to_end(self.dict[key].value)
        # return self.dict[key].value
        node = self.dict[key]
        self.dll.move_to_end(node)
        # print(node[1])
        return node.value[1]
        # return
        # else:
        #     return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # if len(self.dict) == self.limit:
        #     self.dll.remove_from_tail()
        # if key in self.dict:
        #     self.get(key)
        #     self.dict[key] = value
        #     self.dll
        #     self.dll.head.value = value
        # else:
        #     self.dll.add_to_head(value)
        #     self.dict.update({key:value})

        #  Different scenarios
        # if itme/key already exists
        if key in self.dict:
            # overwrite the value
            # where is the value stored?
            self.dict[key].value = (key, value)
            node = self.dict[key]
            # print(node)
            # node = (key, value)
            # move to the tail (most recently used)
            self.dll.move_to_end(node)
            return
        # size is at limit
        if len(self.dll) == self.limit:
            # evict the oldest one
            index_of_oldest = self.dll.head.value[0]
            # print(index_of_oldest)
            del self.dict[index_of_oldest]
            self.dll.remove_from_head()
            # add the new new one to the end

        # size is not at limit
        # if len(self.dll) < self.limit:
        # add to order
        self.dll.add_to_tail((key, value))
        # add it to storage
        # print(self.dll.tail)
        self.dict[key] = self.dll.tail



        # self.dict.update({key:1})
        # if key in self.dict:
        #     # do a get() and then keep size same
        #     self.get(key)
        # self.dll.add_to_head({key:value})
        # self.dict[key] = value
        # if self.size > 10:
        #     self.storage.remove_from_tail()
            # self.dll.add_to_head({key:value})


# import sys
# sys.path.append('../GitHub/Data-Structures/lru_cache')
# from lru_cache import LRUCache
# lru = LRUCache()
# lru.set("k", 5)
# lru.get("k")
# print(lru.get("k"))