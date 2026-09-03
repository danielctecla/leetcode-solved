# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def getLCA(node: 'TreeNode') -> 'TreeNode':
            
            currentValue = node.val
            
            if currentValue > q.val and currentValue > p.val:
                return getLCA(node.left)
            elif currentValue < q.val and currentValue < p.val:
                return getLCA(node.right)
            else:
                return node
        
        return getLCA(root)