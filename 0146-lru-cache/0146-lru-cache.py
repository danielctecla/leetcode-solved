class LRUCache:

    class Node:
        def __init__(self, key: int=0, value: int=0):
            self.key = key
            self.value = value
            self.previous = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = self.Node()
        self.tail = self.Node()

        #Connect initially the nodes
        self.head.next = self.tail
        self.tail.previous = self.head
    
    def _remove_node(self, node: self.Node):
        node.previous.next = node.next
        node.next.previous = node.previous
    
    def _add_front(self, node: self.Node):
        node.next = self.head.next
        node.previous = self.head
        self.head.next.previous = node
        self.head.next = node
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove_node(node)
        self._add_front(node)
        return node.value

    
    def put(self, key: int, value: int):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_front(node)
            return
        
        if len(self.cache) == self.capacity:
            lru = self.tail.previous
            self._remove_node(lru)
            del self.cache[lru.key]
        
        node = self.Node(key, value)
        self._add_front(node)
        self.cache[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# capacity = 2

# {
#     1: 2
#     3: 3
# }

# recent value
# [2]<->[1]<->none

# [1]<->none
# [3]<->[1]<->none