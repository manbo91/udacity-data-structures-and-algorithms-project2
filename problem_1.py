from collections import deque


class Queue:
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.append(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.popleft()
        return None

    def size(self):
        return len(self.q)


class LRU_Cache(object):
    def __init__(self, capacity):
        self.queue = Queue()
        self.cache = dict()
        self.capacity = capacity

    def get(self, key):
        self.update_cache(key)
        return self.cache.get(key, -1)

    def set(self, key, value):
        self.update_cache(key)
        self.cache[key] = value

    def update_cache(self, key):
        self.queue.enq(key)  # use operation

        if self.queue.size() > self.capacity:
            d_key = self.queue.deq()
            if self.queue.size() == 0:
                self.cache = {}
            elif d_key in self.cache and key != d_key:
                del self.cache[d_key]


if __name__ == "__main__":

    # test case 1
    our_cache_1 = LRU_Cache(5)

    our_cache_1.set(1, 1)
    our_cache_1.set(2, 2)
    our_cache_1.set(3, 3)
    our_cache_1.set(4, 4)
    print("Pass" if our_cache_1.get(1) == 1 else "Fail")  # returns 1
    print("Pass" if our_cache_1.get(2) == 2 else "Fail")  # returns 2
    # returns -1 because 9 is not present in the cache
    print("Pass" if our_cache_1.get(9) == -1 else "Fail")
    our_cache_1.set(5, 5)
    our_cache_1.set(6, 6)
    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    print("Pass" if our_cache_1.get(3) == -1 else "Fail")

    # test case 2
    our_cache_2 = LRU_Cache(1)
    our_cache_2.set(1, 1)
    our_cache_2.set(2, 2)
    print("Pass" if our_cache_2.get(2) == 2 else "Fail")  # returns 2
    print("Pass" if our_cache_2.get(1) == -1 else "Fail")  # returns -1

    # test case 3
    our_cache_3 = LRU_Cache(3)
    our_cache_3.set(1, 1)
    our_cache_3.set(2, 2)
    our_cache_3.set(1, 3)
    # returns 3 because changed the cache value
    print("Pass" if our_cache_3.get(1) == 3 else "Fail")

    # test case 4
    our_cache_0 = LRU_Cache(0)
    our_cache_0.set(1, 1)
    print("Pass" if our_cache_0.get(1) == -1 else "Fail")

    # test case 5
    our_cache_2 = LRU_Cache(2)
    our_cache_2.set(1, 1)
    our_cache_2.get(1)
    our_cache_2.get(1)
    our_cache_2.set(3, 3)
    print("Pass" if our_cache_2.get(3) == 3 else "Fail")
