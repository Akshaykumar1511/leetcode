class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        mx,curr=0,0
        for i in nums:
            if i==1:
                curr+=1
            else:
                mx=max(curr,mx)
                curr=0
        mx=max(mx,curr)
        return mx