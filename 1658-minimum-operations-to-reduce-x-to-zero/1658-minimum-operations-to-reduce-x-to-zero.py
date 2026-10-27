class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        s=sum(nums)
        target=s-x
        n=len(nums)
        j=0
        ws=0
        res=float('inf')
        if target<0:
            return -1
        for i in range(n):
            ws+=nums[i]
            while ws>target:
                ws-=nums[j]
                j+=1
            if ws==target:
                res=min(res,n-(i-j+1))
        if math.isinf(res):
            return -1
        else:
            return res  