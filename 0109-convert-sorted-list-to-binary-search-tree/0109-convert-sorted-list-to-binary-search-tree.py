from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        # len of the list 0 to 10^4 - 2000
        # value of the node -10^5 to 10^5

        # getting the middle in current list
        # list max len 2000

        # have the list node in an array
        def build(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None

            mid = (left + right) // 2

            node = TreeNode(arr[mid])

            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)

            return node

        if not head:
            return None

        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        
        return build(0,len(arr)-1)