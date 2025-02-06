class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, num in enumerate(nums):
            diff = target - num 
            if diff in hashmap:
                return [i, hashmap[diff]] 
            hashmap[num] = i 
        
        return []