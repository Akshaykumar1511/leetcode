class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=len(height)
        le,ri=0,l-1
        ans=0
        while le<ri:
            w=ri-le
            h=min(height[ri],height[le])
            a=w*h
            ans=max(ans,a)
            if height[le]>height[ri]:
                ri-=1
            elif height[le]<height[ri]:
                le+=1
            else:
                le+=1
                ri-=1
        return ans