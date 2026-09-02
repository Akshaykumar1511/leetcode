class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen=set()
        i=0
        dist=float('inf')
        seen.add(nums[i])
        for j in range(1,len(nums)):
            while i<j and nums[j] in seen:
                dist=min(dist,j-i)
                seen.remove(nums[i])
                i+=1
            seen.add(nums[j])
        return dist<=k