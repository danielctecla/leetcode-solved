class Node:
	def __init__(self):
		self.val = 0
		self.key = 0
		self.next = None
		self.back = None

class LRUCache:
	def __init__(self, capacity: int):
		self.cache = {}
		self.max_capacity = capacity
		self.capacity = 0
		self.head = Node()
		self.tail = Node()
		
		self.head.next = self.tail
		self.tail.back = self.head
	
	def remove_node(self, node: Node):
		node.next.back = node.back
		node.back.next = node.next
		
	
	def insert_node(self, node: Node):
		node.next = self.head.next
		node.back = self.head
		self.head.next.back = node
		self.head.next = node
		
	
	def put(self, key: int, value: int):
		node = self.cache.get(key, None)
		
		if node:
			node.val = value
			self.remove_node(node)
			self.insert_node(node)
			return
		
		node = Node()
		node.val = value
		node.key = key
		
		if self.capacity == self.max_capacity:
			last_node = self.tail.back
			self.remove_node(last_node)
			del self.cache[last_node.key]
			self.capacity -= 1
		
		self.insert_node(node)
		self.capacity += 1
		self.cache[key] = node

	def get(self, key: int) -> int:
		node = self.cache.get(key,None)
		
		if not node:
			return -1
		
		self.remove_node(node)
		self.insert_node(node)
		
		return node.val