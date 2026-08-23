class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best=0
        for i in range(len(nums)):
            j=i+1
            while j<len(nums):
                curs=(nums[i]-1)*(nums[j]-1)
                best=max(curs,best)
                j+=1
        return best