class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.cache = {}
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        if node == self.head:
            return node.value

        previous_node = node.previous
        next_node = node.next

        if next_node and previous_node:
            next_node.previous = previous_node
            previous_node.next = next_node
        else:
            previous_node.next = None
            self.tail = previous_node
        
        node.previous = None
        node.next = self.head
        self.head.previous = node
        self.head = node
        
        return node.value

    
    def put(self, key: int, value: int):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.get(key)
            return
        
        new_node = self.Node(key,value)
        self.cache[key] = new_node
        self.capacity -= 1

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return

        previous_head = self.head
        previous_head.previous = new_node

        new_node.next = previous_head
        self.head = new_node

        previous_tail = self.tail.previous

        if self.capacity < 0 and previous_tail:
            self.cache.pop(self.tail.key)
            self.tail = previous_tail
            self.tail.next = None  

    class Node:
        def __init__(self, key: int, value: int, next = None, previous = None):
            self.key = key
            self.value = value
            self.previous = previous
            self.next = next


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