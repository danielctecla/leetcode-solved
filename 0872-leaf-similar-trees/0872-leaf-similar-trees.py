# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafs1 = self.getLeafs(root1)
        print(leafs1)
        leafs2 = self.getLeafs(root2)
        print(leafs2)
        return leafs1 == leafs2

    def getLeafs(self,root: TreeNode) -> List[int]:
        leafs = []
        queue = deque()
        queue.append(root)
        
        while queue:
            currentNode = queue.pop()
            if (not currentNode.left) and (not currentNode.right):
                leafs.append(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
            
        return leafs