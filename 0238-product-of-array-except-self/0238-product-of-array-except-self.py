class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        # left pass
        lf=1
        lfa=[1]*len(nums)
        for i in range(len(nums)):
            lfa[i]=lf
            lf*=nums[i]
        
        # right pass
        rf=1
        rfa=[1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            rfa[i]=rf
            rf*=nums[i]
        #merge pass
        for i in range(len(nums)):
            res.append(lfa[i]*rfa[i])
        return res
