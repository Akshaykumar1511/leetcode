# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ot=[True]
        def process(p,q):
            if not q and not p:
                return
            elif (not p and q) or (not q and p):
                ot[0]=False
                return
            elif p.val!=q.val:
                ot[0]=False
                return
            process(p.left,q.left)
            process(p.right,q.right)
        process(p,q)
        return ot[0]