class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        dn=False
        res=[""]*numRows
        i=0
        for char in s:
            res[i]+=char
            if i==0 or i==numRows-1:
                dn=not dn
            
            i+=1 if dn else -1
        return "".join(res)