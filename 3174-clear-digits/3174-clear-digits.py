class Solution:
    def clearDigits(self, s: str) -> str:
        stk=[]
        for i in s:
            if ord(i)>96:
                stk.append(i)
                continue
            else:
                if stk[-1]:
                    stk.pop()
        return "".join(stk)
