class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=float('inf')
        for s in strs:
            if len(s)<l:
                l=len(s)
        i=0
        while i<l:
            for s in strs:
                if s[i]!=strs[0][i]:
                    return strs[0][:i]
            i+=1
        return strs[0][:i]