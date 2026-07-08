class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a=set(nums)
        max_cnt=0
        for i in a:
            if i-1 not in a:
                cnt=1
                b=i+1
                while b in a:
                    cnt+=1
                    b+=1
                if cnt>max_cnt:
                    max_cnt=cnt
        return max_cnt