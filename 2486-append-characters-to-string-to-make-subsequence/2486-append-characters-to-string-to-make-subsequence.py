class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ls,lt=len(s),len(t)
        i,j=0,0
        while i<ls and j<lt:
            if s[i]==t[j]:
                j+=1
            i+=1
        return lt-j