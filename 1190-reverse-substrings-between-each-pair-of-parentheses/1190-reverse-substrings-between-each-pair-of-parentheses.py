class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk=[]
        for i in s:
            if i==")":
                temp=""
                while stk[-1]!="(":
                    temp+=stk.pop()
                stk.pop()
                for j in temp:
                    stk.append(j)
            else:
                stk.append(i)
        return "".join(stk)