class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s=[0]*3 
        for i in nums:
            s[i]+=1
        nums[:s[0]]=[0]*s[0]
        nums[s[0]:s[0]+s[1]]=[1]*s[1]
        nums[s[0]+s[1]:len(nums)]=[2]*s[2]