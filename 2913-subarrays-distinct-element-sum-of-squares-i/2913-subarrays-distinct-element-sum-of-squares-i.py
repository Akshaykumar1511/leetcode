class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        
        # Iterate over all possible starting points of subarrays
        for i in range(n):
            seen = set()
            # Iterate over all possible ending points for the current starting point
            for j in range(i, n):
                seen.add(nums[j])
                # The distinct count is simply the length of our set
                total_sum += len(seen) ** 2
                
        return total_sum