class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        compare=float('inf')
        for i in nums:
            if abs(i)<abs(compare):
                compare=i
            elif abs(i)==abs(compare):
                if i>compare:
                    compare=i
        return compare