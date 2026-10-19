class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        # n=sorted(nums)
        # res=[]
        # for i in range(len(nums)):
        #     if n[i]==target:
        #         res.append(i)
        # return res
        ls_cnt=0
        target_cnt=0
        for i in range(len(nums)):
            if nums[i]<target:
                ls_cnt+=1
            elif nums[i]==target:
                target_cnt+=1
        return list(range(ls_cnt,ls_cnt+target_cnt))