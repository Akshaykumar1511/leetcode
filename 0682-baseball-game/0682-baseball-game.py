class Solution:
    def calPoints(self, operations: List[str]) -> int:
        a=[]
        for i in operations:
            if i == '+':
                s=a[-1]+a[-2]
                a.append(s)
            elif i=='D':
                s=2*a[-1]
                a.append(s)
            elif i=='C':
                a.pop()
            else:
                a.append(int(i))
        return sum(a)