# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root,root.val)]
        
        totalGoodNodes = 0

        while stack:
            current, maxValue = stack.pop()
            
            if current.val >= maxValue:
                maxValue = current.val
                totalGoodNodes += 1
            
            if current.right:
                stack.append((current.right,maxValue))
            if current.left:
                stack.append((current.left,maxValue))
        
        return totalGoodNodes

