class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt=0
        n=len(s)
        l=0
        alcnt={}
        for r in range(n):
            if s[r] in alcnt:
                alcnt[s[r]]+=1
            else:
                alcnt[s[r]]=1
            while ((r-l+1)-max(alcnt.values()))>k:
                alcnt[s[l]]-=1
                l+=1
            ln=(r-l)+1
            cnt=max(cnt,ln)
        return cnt