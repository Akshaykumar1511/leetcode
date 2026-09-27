from collections import Counter
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        counts=Counter(nums)
        uniqueval=sorted(counts.keys())
        res=[]
        max_count=max(counts.values()) if counts else 0
        for i in range(1,max_count+1):
            for j in uniqueval:
                if counts[j]>=i:
                    res.append(j)
        return res