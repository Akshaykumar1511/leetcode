class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        ml,mr=[0]*n,[0]*n
        mx=0
        for i in range(n):
            ml[i]=mx
            mx=max(mx,height[i])
        mx=0
        for i in range(n-1,-1,-1):
            mr[i]=mx
            mx=max(mx,height[i])
        cnt=0
        for i in range(n):
            mn=min(ml[i],mr[i])-height[i]
            if mn>=0:
                cnt+=mn
        return cnt