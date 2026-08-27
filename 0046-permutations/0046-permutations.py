class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def back():
            if len(res)==len(nums):
                sol.append(res[:])
                return
            for i in nums:
                if i not in res:
                    res.append(i)
                    back()
                    res.pop()

        sol,res=[],[]
        back()
        return sol