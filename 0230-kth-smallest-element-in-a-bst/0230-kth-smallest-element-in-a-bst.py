# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=[None]
        a=[k]
        def helper(node):
            if not node:
                return None
            helper(node.left)
            a[0]-=1
            if a[0]==0:
                ans[0]=node.val
            helper(node.right)
        helper(root)
        return ans[0]
