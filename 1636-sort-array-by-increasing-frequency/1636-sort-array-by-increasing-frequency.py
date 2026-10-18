from collections import Counter
class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        cnt=Counter(nums)
        # cn=sorted(cnt.items(),key=lambda item:(item[1],-item[0]))
        # res=[]
        # for i,v in cn:
        #     lc=[i]*v
        #     res.extend(lc)
        # return res
        return sorted(nums,key=lambda x:(cnt[x],-x))