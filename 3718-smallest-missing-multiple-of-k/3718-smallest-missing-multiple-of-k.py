class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        a = set(nums)
        i = k
        while i in a:
            i += k
        return i
