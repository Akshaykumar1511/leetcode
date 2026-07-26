from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnts1=Counter(s1)
        l=0
        ans=False
        for r in range(len(s1),len(s2)+1):
            s=s2[l:r]
            if cnts1==(Counter(s)):
                ans=True
            l+=1
        return ans