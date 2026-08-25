from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        frac=n/3
        count=Counter(nums)
        res=[]
        for i,v in count.items():
            if v>frac:
                res.append(i)
        return res