# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        maxDepth = 1

        stack = []
        stack.append((root,1))
        while stack:
            current = stack.pop()
            if current[1] > maxDepth:
                maxDepth = current[1]
            if current[0].left:
                stack.append((current[0].left, current[1] + 1))
            if current[0].right:
                stack.append((current[0].right, current[1] + 1))
        
        return maxDepth
        

        