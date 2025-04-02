class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        L = 0
        R = len(numbers) - 1
        while L < R:
            currSum = numbers[L] + numbers[R]
            if currSum > target:
                R -= 1
            elif currSum < target:
                L += 1
            else:
                return [L + 1, R + 1]
        return []
            
# TC: O(N)
# SC: O(1)