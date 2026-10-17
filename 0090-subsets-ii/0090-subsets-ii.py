class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        # def back(i):
        #     if i == len(nums):
        #         res.add(tuple(sorted(sol[:])))
        #         return
        #     back(i+1)
        #     sol.append(nums[i])
        #     back(i+1)
        #     sol.pop()

        # sol,res=[],set()
        # back(0)
        # return list(res)
        def back(i):
            if i==len(nums):
                res.append(sol[:])
                return
            sol.append(nums[i])
            back(i+1)
            sol.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            back(i+1)
        nums.sort()
        res,sol=[],[]
        back(0)
        return res