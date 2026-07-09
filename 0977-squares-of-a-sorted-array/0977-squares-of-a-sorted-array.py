class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ln=len(nums)
        ans=[]
        l,r=0,ln-1
        while l<=r:
            if abs(nums[r])>=abs(nums[l]):
                ans.append(nums[r]**2)
                r-=1
            else:
                ans.append(nums[l]**2)
                l+=1
        l,r=0,ln-1
        while l<=r:
            a=ans[r]
            ans[r]=ans[l]
            ans[l]=a
            l+=1
            r-=1
        return ans
