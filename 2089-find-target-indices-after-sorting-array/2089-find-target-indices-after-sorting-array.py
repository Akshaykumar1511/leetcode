class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        n=sorted(nums)
        res=[]
        for i in range(len(nums)):
            if n[i]==target:
                res.append(i)
        return res