class Solution:
    def median(arr):
        n=len(arr)
        if n%2==0:
            return (arr[n//2]+arr[(n//2)+1])/2
        return arr[n//2]
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return median(sorted(nums1+nums2))