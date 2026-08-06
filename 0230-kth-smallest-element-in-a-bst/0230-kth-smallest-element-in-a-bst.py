# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=[]
        def traverse(root):
            if not root:
                return
            if root.val not in ans:
                ans.append(root.val)
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        ans.sort()
        return ans[k-1]