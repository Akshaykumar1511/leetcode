from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        dq=deque()
        dq.append(root)
        ans=[]
        while dq:
            lst=[]
            n=len(dq)
            for i in range(n):
                node=dq.popleft()
                lst.append(node.val)
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            ans.append(lst)
        return ans