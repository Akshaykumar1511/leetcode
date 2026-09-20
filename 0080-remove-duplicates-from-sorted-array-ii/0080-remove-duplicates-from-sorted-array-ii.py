from collections import defaultdict
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        d=defaultdict(int)
        j=0
        for i,v in enumerate(nums):
            d[v]+=1
            if d[v]<=2:
                nums[j]=nums[i]
                j+=1
            else:
                continue
        return j
                