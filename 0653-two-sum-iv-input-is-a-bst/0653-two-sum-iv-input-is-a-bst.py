# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen=set()
        def rec(node):
            if not node:
                return False
            if rec(node.left):
                return True
            tar=k-(node.val)
            if tar in seen:
                return True
            seen.add(node.val)
            return rec(node.right)
        return rec(root)