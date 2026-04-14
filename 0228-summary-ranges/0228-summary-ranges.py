class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ot=[]
        j= None
        for i in range(len(nums)):
            if j==None:
                j=nums[i]
            if i==len(nums)-1 or nums[i+1]!=nums[i]+1:
                if nums[i]==j:
                    ot.append(str(nums[i]))
                    j=None
                else:
                    ot.append(str(f"{j}->{nums[i]}"))
                    j=None
        return ot