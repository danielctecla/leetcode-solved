from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        
        # node <-
        # input is tree
        # output bool -> True when the tree is complete
        # there is an exeption return False when the last level
        # the nodes aren't to the left

        # level = 0
        # queue = first node
        # while queue:
        #   necessary_nodes = 2 ** level
        #   len of the queue -> current nodes
        #   new_nodes empty
        #   for _ in range(current_nodes):
        #       popleft node
        # 
        #       if (node left or node rigth) and current_nodes != necessary_nodes
        #           return False
        #       if node right and not node left:
        #           return False
        #       if node left
        #           add new_nodes left
        #       id node rigth
        #           add new_nodes rigth
        #    level += 1
        #       
        #    queue = new_nodes
        #    
        # return True

        # [1,2,3,4,5,6]

        # level 1
        # queue 
        # new queue 45
        # 3
        # necessary nodes = 2
        # current nodes = 2
        queue = deque()
        queue.append(root)
        gap = False
        while queue:
            number_nodes = len(queue)

            for _ in range(number_nodes):
                node = queue.popleft()
                
                if gap and (node.left or node.right):
                    return False
                if not node.left and node.right:
                    return False
                if not node.left or not node.right:
                    gap = True
                


                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        
        return True

                 