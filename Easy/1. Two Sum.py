class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[num], i]
            prevMap[num] = i
        return []
    
    # TC: O(N)
    # SC: O(N)