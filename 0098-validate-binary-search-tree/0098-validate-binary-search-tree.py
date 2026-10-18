# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        def retrieveRanges(node):
            if node is None:
                return True, float("inf"), float("-inf")

            left_valid, left_min, left_max = retrieveRanges(node.left)
            right_valid, right_min, right_max = retrieveRanges(node.right)

            if not left_valid or not right_valid:
                return False, 0, 0

            if left_max >= node.val or right_min <= node.val:
                return False, 0, 0

            minimum = min(left_min, node.val)
            maximum = max(right_max, node.val)

            return True, minimum, maximum

        valid, _, _ = retrieveRanges(root)
        return valid