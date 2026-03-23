class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof=maxval=prof=0
        minval=float('inf')
        for i in prices:
            if i<minval:
                minval=i
                maxval=0
            else:
                prof=i-minval
                if prof>maxprof:
                    maxprof=prof
                if i>maxval:
                    maxval=i
        return maxprof