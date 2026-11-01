class Solution:
    def minMoves(self, nums: list[int]) -> int:
        smallest=min(nums)
        k=0
        for i in nums:
            k+=i-smallest
        return k