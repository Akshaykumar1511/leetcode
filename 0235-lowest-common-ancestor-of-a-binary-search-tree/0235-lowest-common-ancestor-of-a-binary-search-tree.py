# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca=[root]
        def match(root,p,q):
            if not root:
                return
            lca[0]=root
            if root is p or root is q:
                return
            elif root.val<p.val and root.val<q.val:
                match(root.right,p,q)
            elif root.val>p.val and root.val>q.val:
                match(root.left,p,q)
            else: return
        match(root,p,q)
        return lca[0]