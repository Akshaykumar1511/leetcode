from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=Counter(nums)
        ln=len(nums)/2
        most_rep=a.most_common(1)
        if most_rep[0][1]>ln:
            return most_rep[0][0]