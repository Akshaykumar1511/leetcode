class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        ml,mr=[0]*n,[0]*n
        lm,rm=0,0
        for i in range(n):
            j=-i-1
            ml[i],mr[j]=lm,rm
            lm=max(lm,height[i])
            rm=max(rm,height[j])
        cnt=0
        for i in range(n):
            cap=min(ml[i],mr[i])
            cnt+=max(0,cap-height[i])
        return cnt