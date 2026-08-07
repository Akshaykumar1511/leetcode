# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def match(root,subRoot):
            if not root and not subRoot:
                return True
            elif not root or not subRoot:
                return False
            elif root.val!=subRoot.val:
                return False
            return match(root.left,subRoot.left) and match(root.right,subRoot.right)
        def same(root,subRoot):
            if not root:
                return False
            elif match(root,subRoot):
                return True
            return same(root.left,subRoot) or same(root.right,subRoot)
        return same(root,subRoot)