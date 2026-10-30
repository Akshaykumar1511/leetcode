class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk=[]
        for i in num:
            while k>0 and stk and stk[-1]>i:
                k-=1
                stk.pop()
            stk.append(i)
        if k>0:
            stk=stk[:-k]
        res= "".join(stk).lstrip("0")
        return res if res else "0"