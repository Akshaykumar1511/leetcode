class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def back(i):
            if i==len(nums):
                res.append(sol[:])
                return
            #dont pick anything
            back(i+1)
            #pick
            sol.append(nums[i])
            back(i+1)
            sol.pop()
        sol,res=[],[]
        back(0)
        return res