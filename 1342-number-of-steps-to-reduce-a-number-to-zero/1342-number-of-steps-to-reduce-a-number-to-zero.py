class Solution:
    def numberOfSteps(self, num: int) -> int:
        step=0
        cur=num
        while cur>0:
            step+=1
            if cur%2==0:
                cur=cur/2
            else:
                cur-=1
        return step