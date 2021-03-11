# Problem 3: Huffman Coding

## huffman_encoding()

### Worst-case time-complexity of `huffman_encoding()` is **_O(n log n)_**.

First, we need the frequency of each character. So, I made `get_frequencies()`.

Worst-case time-complexity of `get_frequencies()` is **_O(n)_** because we are iterating the each character from data.

And I am appending `(frequency, index, character)` to heap data structure. `index` is the order first each character from data. if frequency same case, it compares index. Worst-case time-complexity of appending to heap data structure is **_O(n log n)_**.

Next, I build the tree.

```python
# ~

node_index = len(data) # To avoid collision with character indexes
while len(heap) > 1: # O(1)
    min_1 = heapq.heappop(heap) # O(log n)
    min_2 = heapq.heappop(heap) # O(log n)
    value = min_1[0] + min_2[0] # O(1)
    node = Node(value) # O(1)
    node.left = min_1 # O(1)
    node.right = min_2 # O(1)
    heapq.heappush(heap, (value, node_index, node)) # O(log n)
    node_index += 1 # O(1)

# O(n - 1) * O(3 log n + 6)
# O(n log n) + O(6n)
# O(n log n)

# ~
```

The time-complexity of the code above is **_O(n log n)_**. Because we take two out of the heap and put one back. In this worst-case is all character different.
So **_O(n-1)_** becomes **_O(n)_**. So worst-case time-compleixty is **_O(n log n)_**.

Next, I made `get_huffman_codes()`.

```python
def get_huffman_codes(tree):
    """Returns `dict` storing the huffman code from a Huffman Tree"""
    huffman_codes = dict()

    def traverse(root, code):
        if root is None:
            return

        if type(root) is str:
            huffman_codes[root] = code
            return

        traverse(root.left[2], code+"0")
        traverse(root.right[2], code+"1")

    traverse(tree.get_root(), "")
    return huffman_codes
```

The time-complexity of `get_huffman_codes()` is **_O(n log n)_** because we are traversing all characters.

```python
huffman_codes = get_huffman_codes(tree)
encoded_data = [huffman_codes[char] for char in data] # O(n)
encoded_data = "".join(encoded_data) # O(n)
return encoded_data, tree
```

The time-complexity of the above code is **_O(n)_**.

Finally, the most complex thing in this code is **_O(n log n)_**, so the time-complexity of `huffman_encoding()` is **_O(n log n)_**.

### Worst-case space-complexity of `huffman_encoding()` is **_O(n)_**.

The worst-case is all characters different. So, `frequencies` is **_O(n)_**, `chars_order` is **_O(n)_**, `heap` is **_O(n)_** and `tree` is **_O(n-1)_** -> **_O(n)_**.

Therefore, **_O(4n)_** becomes **_O(n)_**.

## huffman_decoding()

### Worst-case time-complexity of `huffman_decoding()` is **_O(n log n)_**

Because we have to iterate elements from data. And we have to find the right character in the binary tree structure.

### Worst-case space-complexity of `huffman_decoding()` is **_O(n)_**.

In the worst-case, `data` and `decoded_string` are becoming the same lengths. So, the worst-case space-complexity of this program is **_O(n)_**.
