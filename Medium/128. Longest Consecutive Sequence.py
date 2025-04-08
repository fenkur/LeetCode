class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        myset = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in myset:
                length = 0
                while (n + length) in myset:
                    length += 1
                longest = max(longest, length)
        return longest


# TC: O(N)
# SC: O(N)

        