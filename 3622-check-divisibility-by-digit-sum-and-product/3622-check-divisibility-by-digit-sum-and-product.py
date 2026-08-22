class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summ,pro=0,1
        num=str(n)
        for i in range(len(num)):
            summ+=int(num[i])
            pro*=int(num[i])
        tot=summ+pro
        return n%(tot)==0