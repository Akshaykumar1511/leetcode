class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cnt=float("inf")
        l=0
        n=len(nums)
        summ=0
        for r in range(n):
            summ+=nums[r]
            while summ>=target:
                cnt=min(cnt,(r-l+1))
                summ-=nums[l]
                l+=1
        return cnt if cnt!=float('inf') else 0