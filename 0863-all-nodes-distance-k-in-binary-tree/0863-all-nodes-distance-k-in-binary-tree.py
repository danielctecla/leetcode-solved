# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_map = {}
        
        def get_parent(root): 
            if root.left:
                parent_map[root.left] = root
                get_parent(root.left)
            
            if root.right:
                parent_map[root.right] = root
                get_parent(root.right)
            
        get_parent(root)
        
        ans = []
        queue = deque([target])
        visited = set()
        
        while k and queue:
            k -= 1
            for i in range(len(queue)):
                node = queue.popleft()
                visited.add(node)
                
                if node.left and node.left not in visited:
                    queue.append(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)
                
                parent_node = parent_map.get(node,None)
                
                if parent_node and parent_node not in visited:
                    queue.append(parent_node)
        if k:
            return []
        
        for node in queue:
            ans.append(node.val)
        
        return ans