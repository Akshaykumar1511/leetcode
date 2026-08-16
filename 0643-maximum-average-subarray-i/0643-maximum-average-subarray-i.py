class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curs=0
        maxavg=0
        for i in range(k):
            curs+=nums[i]
        maxavg=curs
        for i in range(k,len(nums)):
            curs+=nums[i]
            curs-=nums[i-k]
            maxavg=max(maxavg,curs)
        return maxavg/k