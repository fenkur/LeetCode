class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = sorted(nums1 + nums2)
        n = len(nums3)
        if n % 2 == 0:
            mid = n // 2
            return (nums3[mid] + nums3[mid-1]) / 2.0
        else:
            mid = n // 2
            return float(nums3[mid])
            
# Time Complexity: O((m+n) * log(m+n)) 
# Space Complexity: O(m + n)         

