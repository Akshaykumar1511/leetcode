class Solution:
    def scoreOfString(self, s: str) -> int:
        i=0
        summ=0
        for j in range(1,len(s)):
            summ+=abs(ord(s[i])-ord(s[j]))
            i+=1
        return summ