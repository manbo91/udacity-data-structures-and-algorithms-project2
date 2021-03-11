import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash=0):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def get_data(self):
        return self.data

    def get_hash(self):
        return self.hash

    def get_timestamp(self):
        return self.timestamp

    def get_previous_hash(self):
        return self.previous_hash

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


class BlockChain:

    def __init__(self):
        self.blocks = LinkedList()

    def get_block(self, hash_value):
        node = self.blocks.get_head()
        if node:
            block = node.get_data()
            if block.get_hash() == hash_value:
                return block
        return None

    def add_block(self, data):
        node = self.blocks.get_head()

        timestamp = datetime.now().strftime('%H:%M %d/%m/%Y')
        if node is None:
            self.blocks.append(Block(timestamp, data))
        else:
            block = node.get_data()
            self.blocks.append(Block(timestamp, data, block.get_hash()))

        return self.blocks.get_head().get_data().get_hash()

    def get_block_to_array(self):
        arr = list()

        node = self.blocks.get_head()
        while node:
            block = node.get_data()
            arr.append(block.get_data())
            node = node.next
        return arr

    def print_block_history(self):
        node = self.blocks.get_head()
        while node:
            block = node.get_data()
            print(
                f"data: {block.get_data()}\nhash: {block.get_hash()}\ntimestamp: {block.get_timestamp()}")
            print("-----------------------")
            node = node.next


if __name__ == "__main__":
    block_history = list()
    block_chain = BlockChain()

    data = "Some Information"
    current_hash = block_chain.add_block(data)
    block_history.append(data)

    data = "Udacity"
    current_hash = block_chain.add_block(data)
    block_history.append(data)

    data = "Blockchain"
    current_hash = block_chain.add_block(data)
    block_history.append(data)

    block_chain.print_block_history()
    # test case 1
    print("Pass" if block_chain.get_block(
        current_hash).get_data() == data else "Fail")
    # test case 2
    print("Pass" if block_chain.get_block(
        current_hash).get_hash() == current_hash else "Fail")
    # test case 3
    print("Pass" if block_chain.get_block_to_array()
          == list(reversed(block_history)) else "Fail")
