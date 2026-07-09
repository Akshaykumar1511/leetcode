class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force n^2 not accepted
        # l=len(temperatures)
        # fin=[0]*l
        # for i in range(l):
        #     cnt=0
        #     j=i+1
        #     while j<l:
        #         if temperatures[i]>=temperatures[j]:
        #             cnt+=1
        #             j+=1
        #         else:
        #             fin[i]=cnt+1
        #             break
        # return fin
        temps=temperatures
        n=len(temps)
        ans=[0]*n
        stk=[]
        for i,v in enumerate(temps):
            while stk and stk[-1][1]<v:
                stk_i,stk_v=stk.pop()
                ans[stk_i]=i-stk_i
            stk.append((i,v))
        return ans