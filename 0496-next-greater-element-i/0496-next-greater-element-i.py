class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans=[-1]*len(nums1)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    j+=1
                    curr=nums1[i]
                    while j<len(nums2):
                        if ans[i]==-1 and nums2[j]>curr:
                            ans[i]=nums2[j]
                            break
                        j+=1

        return ans