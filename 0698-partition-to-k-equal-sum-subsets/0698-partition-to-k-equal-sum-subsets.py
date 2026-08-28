class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # summ=sum(nums)
        # if summ%k!=0:
        #     return False
        # target=summ//k
        # nums.sort(reverse=True)
        # if nums[0]>target:
        #     return False
        
        # def back(k_l,curbs,i):
        #     if k_l==1:
        #         return True
        #     if curbs==target:
        #         return back(k_l-1,0,0)
        #     for j in range(i,len(nums)):
        #         if seen[j]==1:
        #             continue
        #         if curbs+nums[j]>target:
        #             continue
                
        #         seen[j]=1

        #         if back(k_l,curbs+nums[j],j+1):
        #             return True
                
        #         seen[j]=0

        #     return False

        # seen=[0]*len(nums)
        # if back(k,0,0):
        #     return True
        # else:
        #     return False

        target=sum(nums)
        if target%k!=0:
            return False
        target=target//k
        nums.sort(reverse=True)
        if nums[0]>target:
            return False
        seen=[0]*len(nums)
        def back(k,cursum,i):
            if k==0:
                return True
            if cursum==target:
                return back(k-1,0,0)
            for j in range(i,len(nums)):
                if seen[j]==1 or cursum+nums[j]>target:
                    continue
                seen[j]=1
                if back(k,cursum+nums[j],j+1):
                    return True
                seen[j]=0
                if cursum==0: break
            return False

        return back(k,0,0)