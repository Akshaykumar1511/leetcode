class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        best=0
        n=len(nums)
        zeros=0
        l=0
        for r in range(n):
            if nums[r]==0:
                zeros+=1
            while zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            ln=(r-l)+1
            best=max(best,ln)
        return best