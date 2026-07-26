class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett=set()
        n=len(s)
        cnt=0
        l=0
        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            ln=(r-l)+1
            cnt=max(cnt,ln)
            sett.add(s[r])
        return cnt