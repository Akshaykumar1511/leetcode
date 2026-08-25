class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum={0:1}
        cursum=0
        res=0
        for i in nums:
            cursum+=i
            res+=prefixSum.get(cursum-k,0)
            prefixSum[cursum]=prefixSum.get(cursum,0)+1
        return res