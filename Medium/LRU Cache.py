class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key in self.d:
            n = self.d[key]
            self.remove(n)
            self.add(n)
            return n.val
        return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
        n = Node(key,value)
        self.add(n)
        self.d[key] = n
        if len(self.d) > self.capacity:
            n = self.head.next
            self.remove(self.head.next)
            del self.d[n.key]
        
    def add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = p
            
    def remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None