class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            j=i
            k=0
            while k<len(needle) and j<len(haystack) and needle[k]==haystack[j]:
                j+=1
                k+=1
                if k==len(needle):
                    return i
        return -1