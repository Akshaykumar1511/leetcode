class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        co=0
        res=""
        for i in s:
            if i=="(":
                if co>=1:
                    res+=i
                co+=1
            elif i==")":
                if co>=2:
                    res+=i
                co-=1
        return res