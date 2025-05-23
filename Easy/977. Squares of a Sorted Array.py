class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l, r = 0, len(nums) - 1
        result = []
        
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                result.append(nums[l] ** 2)
                l += 1
            else:
                result.append(nums[r] ** 2)
                r -= 1
        
        result.reverse()
        return result

# TC: O(N)
# SC: O(N)