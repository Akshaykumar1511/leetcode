class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        summ=0
        cnt=float('inf')
        for r in range(len(nums)):
            summ+=nums[r]
            while summ>=target:
                ln=(r-l)+1
                cnt=min(cnt,ln)
                summ-=nums[l]
                l+=1
        return cnt if not cnt==float('inf') else 0
                