class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans=[]
        i=0
        while i<len(nums):
            sum=nums[i]
            while i<len(nums)-1 and nums[i+1]==nums[i]+1:
                i+=1
            if nums[i]==sum:
                ans.append(str(sum))
            else:
                ans.append(str(sum)+"->"+str(nums[i]))
            i+=1
        return ans