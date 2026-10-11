class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sm=0
        n=len(nums)
        for i in range(n):
            if n%(i+1)==0:
                sm+=nums[i]**2
        return sm