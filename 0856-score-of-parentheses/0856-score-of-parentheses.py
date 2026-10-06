class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk=[0]
        for i in s:
            if i=="(":
                stk.append(0)
            else:
                cs=stk.pop()
                stk[-1]+=max(cs*2,1)
        return stk[-1]