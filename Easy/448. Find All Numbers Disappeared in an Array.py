class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numset = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in numset]

nums = [4,3,2,7,8,2,3,1]

example = Solution()
print(example.findDisappearedNumbers(nums))
        
            
        