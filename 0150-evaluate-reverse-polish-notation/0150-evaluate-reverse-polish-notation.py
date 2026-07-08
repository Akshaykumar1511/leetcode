class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a=[]
        for i in tokens:
            if i == '+':
                s=a[-2]+a[-1]
                a.pop()
                a.pop()
                a.append(s)
            elif i=='-':
                s=a[-2]-a[-1]
                a.pop()
                a.pop()
                a.append(s)
            elif i=='*':
                s=a[-2]*a[-1]
                a.pop()
                a.pop()
                a.append(s)
            elif i=='/':
                s=int(a[-2]/a[-1])
                a.pop()
                a.pop()
                a.append(s)
            else:
                a.append(int(i))
        return a[0]