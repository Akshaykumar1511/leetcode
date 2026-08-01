class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        a=[0]*len(temperatures)
        stk=[]
        for i in range(len(temperatures)):
            while stk and temperatures[i]>temperatures[stk[-1]]:
                b=stk.pop()
                a[b]=(i-b)
            stk.append(i)
        return a