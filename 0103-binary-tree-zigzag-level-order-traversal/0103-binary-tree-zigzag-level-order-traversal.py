from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        left_to_right=True
        if not root:
            return []
        q.append(root)
        res=[]
        while q:
            curl=deque()
            for _ in range(len(q)):
                curr=q.popleft()
                if left_to_right:
                    curl.append(curr.val)
                else:
                    curl.appendleft(curr.val)
                if curr.left:
                    q.append(curr.left)  
                if curr.right:
                    q.append(curr.right)
                
            res.append(list(curl))
            left_to_right=not left_to_right 
        return res