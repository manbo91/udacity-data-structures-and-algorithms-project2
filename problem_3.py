import sys
import heapq


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None


class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def set_root(self, node):
        self.root = node


def get_frequencies(data):
    """Returns `dict` containing the count of characters"""
    chars_count = dict()
    chars_order = []
    for char in data:
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1
            chars_order.append(char)
    return chars_count, chars_order


def get_huffman_codes(tree):
    """Returns `dict` storing the huffman code from a Huffman Tree"""
    huffman_codes = dict()

    def traverse(root, code):
        if root is None:
            return

        if type(root) is str:
            huffman_codes[root] = code
            return

        if root.has_left_child():
            traverse(root.left[2], code+"0")
        if root.has_right_child():
            traverse(root.right[2], code+"1")

    traverse(tree.get_root(), "")
    return huffman_codes


def huffman_encoding(data):
    if data is None:
        raise ValueError("The data of arguments must be a string.")
    if data == "":
        empty_tree = Tree()
        return "", empty_tree

    frequencies, chars_order = get_frequencies(data)

    heap = []
    for i, char in enumerate(chars_order):
        heapq.heappush(heap, (frequencies[char], i, char))

    node_index = len(data)  # To avoid collision with character indexes
    if len(heap) == 1:
        min_1 = heapq.heappop(heap)
        value = min_1[0]
        node = Node(value)
        node.left = min_1
        heapq.heappush(heap, (value, node_index, node))
    else:
        while len(heap) > 1:
            min_1 = heapq.heappop(heap)
            min_2 = heapq.heappop(heap)
            value = min_1[0] + min_2[0]
            node = Node(value)
            node.left = min_1
            node.right = min_2
            heapq.heappush(heap, (value, node_index, node))
            node_index += 1

    _, _, root_node = heap[0]
    tree = Tree()
    tree.set_root(root_node)

    huffman_codes = get_huffman_codes(tree)
    encoded_data = [huffman_codes[char] for char in data]
    encoded_data = "".join(encoded_data)
    return encoded_data, tree


def huffman_decoding(data, tree):
    decoded_string = list()

    index = 0
    node = tree.get_root()
    while index <= len(data):
        if type(node) is str:
            decoded_string.append(node)
            node = tree.get_root()

        if index == len(data):
            break

        bit = data[index]
        if bit == "0":
            node = node.left[2]
        else:  # bit == "1"
            node = node.right[2]

        index += 1

    return "".join(decoded_string)


if __name__ == "__main__":
    codes = {}

    # test case 1
    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    print("Pass\n" if a_great_sentence == decoded_data else "False\n")

    # test case 2
    a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    print("Pass\n" if a_great_sentence == decoded_data else "False\n")

    # test case 3
    a_great_sentence = "In general, a data compression algorithm reduces the amount of memory"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    print("Pass\n" if a_great_sentence == decoded_data else "False\n")

    # test case 4
    a_great_sentence = "aa"

    print("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)

    print("The content of the encoded data is: {}\n".format(decoded_data))

    print("Pass\n" if a_great_sentence == decoded_data else "False\n")

    # test case 5
    a_great_sentence = ""

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    print("Pass\n" if a_great_sentence == decoded_data else "False\n")
