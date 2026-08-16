class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        n=len(s)
        seen=set()
        l=0
        for i in range(n):
            while s[i] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[i])
            maxlen=max(maxlen,(i-l)+1)
        return maxlen