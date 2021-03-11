# Problem 1: LRU Cache

## Worst-case time-complexity is **_O(1)_**.

Queue data structures are used to track the order in which the cache is used. And the cache key values are stored in a dictionary.

```python
def get(self, key):
    if key if self.cache:
        self.update_cache(key)
        return self.cache[key]
    return -1
```

The time complexity of `get()` is the time complexity of accessing the dictionary and the `update_cache()` function.

The time complexity of accessing a dictionary value is **_O(1)_**.

```python
def update_cache(self, key):
    self.queue.enq(key) # use operation
    if self.queue.size() > self.capacity:
        d_key = self.queue.deq()
        del self.cache[d_key]
```

The time complexity of `queue.enq()`, `queue.deq()` and `queue.size()` are all **_O(1)_**, and `del` is also **_O(1)_**. So the time complexity of `update_cache()` is **_O(1)_**.

Therefore, the time complexity of `get()` is **_O(1)_**.

```python
def set(self, key, value):
    self.update_cache(key)
    self.cache[key] = value
```

The time complexity of adding values to the dictionary is **_O(1)_**.
The time complexity of `update_cache()` checked above is **_O(1)_**, so the time complexity of `set()` is **_O(1)_**.

## Worst-case space-complexity is O(n).

We are storing the values in the `queue` and `dict` with a limit of the capacity we set. We are storing cache order in the `queue` and value in the `dict`.

The space-complexity of `queue` is O(n) and the space-complexity of `dict` is O(n). Total is O(2n)

Therefore, the space-complexity of this program is O(n).
n = capacity.
