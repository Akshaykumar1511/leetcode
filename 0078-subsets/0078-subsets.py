class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        sol,res=[],[]

        def backtrack(i):
            if n==i:
                res.append(sol[:])
                return
            #dont pick the num
            backtrack(i+1)

            #pick the number
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return res