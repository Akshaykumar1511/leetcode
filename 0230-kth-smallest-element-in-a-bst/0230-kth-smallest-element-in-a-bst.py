# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # ans=[]
        # def traverse(root):
        #     if not root:
        #         return
        #     if root.val not in ans:
        #         ans.append(root.val)
        #     traverse(root.left)
        #     traverse(root.right)
        # traverse(root)
        # ans.sort()
        # return ans[k-1]
        
        #method 2
        # count=[k]
        # ans=[0]
        # def rec(root):
        #     if not root:
        #         return
        #     rec(root.left)
        #     if count[0]==1:
        #         ans[0]=root.val
        #     count[0]-=1
        #     if count[0]>0:
        #         rec(root.right)
        # rec(root)
        # return ans[0]

        count=[k]
        def rec(root):
            if not root:
                return None
            ans=rec(root.left)
            if ans is not None:
                return ans
            count[0]-=1
            if count[0]==0:
                return root.val
            return rec(root.right)
        return rec(root)