class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[]
        summ=0
        for i in nums:
            summ+=i
            res.append(summ)
        return res