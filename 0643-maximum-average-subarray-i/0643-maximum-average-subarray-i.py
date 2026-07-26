class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ=0
        best=float('-inf')
        for i in range(0,k):
            summ+=nums[i]
        avgg=summ/k
        best=max(best,avgg)
        for j in range(k,len(nums)):
            summ+=nums[j]
            summ-=nums[j-k]
            avgg=summ/k
            best=max(best,avgg)
        return best