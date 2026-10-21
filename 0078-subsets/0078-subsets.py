class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def back(i):
            if i==len(nums):
                res.append(sol[:])
                return
            back(i+1)
            sol.append(nums[i])
            back(i+1)
            sol.pop()
        res,sol=[],[]
        back(0)
        return res