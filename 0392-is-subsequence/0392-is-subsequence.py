class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S=len(s)
        T=len(t)
        j=0
        if S>T: return False
        if S==0: return True
        for i in range(T):
            if s[j]==t[i]:
                if j==S-1:
                    return True
                else:
                    j+=1
        return False