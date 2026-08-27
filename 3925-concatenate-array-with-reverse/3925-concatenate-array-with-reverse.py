class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        res=[]
        res.extend(nums)
        for i in range(len(nums)-1,-1,-1):
            res.append(nums[i])
        return res