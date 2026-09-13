# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans=float('inf')
        def back(curr,node):
            if not node:
                return
            if not node.right and not node.left:
                nonlocal ans
                ans=min(ans,curr+1)
            back(curr+1,node.left)
            back(curr+1,node.right)
        back(0,root)
        return ans