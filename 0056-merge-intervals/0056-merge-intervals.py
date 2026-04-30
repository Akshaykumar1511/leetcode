class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[intervals[0]]
        for i in range(1,len(intervals)):
            lst=res[-1]
            if lst[1] >= intervals[i][0]:
                res[-1][1]=max(intervals[i][1],lst[1])
            else:
                res.append(intervals[i])
        return res