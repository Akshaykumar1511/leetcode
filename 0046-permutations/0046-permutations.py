class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        sol,res=[],[]
        def backtrack():
            if n==len(sol):
                res.append(sol[:])
                return
            for i in nums:
                if i not in sol:
                    sol.append(i)
                    backtrack()
                    sol.pop()
        backtrack()
        return res