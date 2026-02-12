class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        i=0
        j=n-1
        while i<=j:
            if nums[i]==val:
                if nums[j]!=val:
                    nums[i]=nums[j]
                    j-=1
                    i+=1
                    n-=1
                else:
                    j-=1
                    n-=1
            else:
                i+=1
        return n