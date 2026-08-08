# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # ans=[None]
        # a=[k]
        # def helper(node):
        #     if not node:
        #         return None
        #     helper(node.left)
        #     a[0]-=1
        #     if a[0]==0:
        #         ans[0]=node.val
        #     helper(node.right)
        # helper(root)
        # return ans[0]
        cur=[k]
        def helper(node):
            if not node:
                return None
            ans=helper(node.left)
            if ans is not None:
                return ans
            cur[0]-=1
            if cur[0]==0:
                return node.val
            return helper(node.right)
        return helper(root)