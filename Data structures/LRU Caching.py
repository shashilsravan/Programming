class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hash:
            node = self.hash[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.remove(self.hash[key])
        node = Node(key, value)
        self.insert(node)
        self.hash[key] = node
        if len(self.hash) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.hash[node.key]

    def remove(self, node):
        prevN = node.prev
        nextN = node.next
        prevN.next = nextN
        nextN.prev = prevN

    def insert(self, node):
        self.tail.prev.next, node.next = node, self.tail
        self.tail.prev, node.prev = node, self.tail.prev

