# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_map = {}

        def build_parent_map(node):
            if not node:
                return

            if node.left:
                parent_map[node.left] = node
                build_parent_map(node.left)

            if node.right:
                parent_map[node.right] = node
                build_parent_map(node.right)

        build_parent_map(root)

        queue = deque([target])
        visited = {target}

        while queue and k > 0:
            for _ in range(len(queue)):
                node = queue.popleft()

                neighbors = [
                    node.left,
                    node.right,
                    parent_map.get(node)
                ]

                for neighbor in neighbors:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            k -= 1

        return [node.val for node in queue]