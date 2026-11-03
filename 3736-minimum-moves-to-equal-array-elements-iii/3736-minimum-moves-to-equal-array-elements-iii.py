class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mn=max(nums)
        res=0
        for i in nums:
            res+=(mn-i)
        return res