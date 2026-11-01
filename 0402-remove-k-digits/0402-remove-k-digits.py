class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk=[]
        for i in num:
            while k>0 and stk and stk[-1]>i:
                stk.pop()
                k-=1
            stk.append(i)
        if k>0:
            stk=stk[:-k]
        stk=("".join(stk)).lstrip("0")
        return stk if stk else "0"