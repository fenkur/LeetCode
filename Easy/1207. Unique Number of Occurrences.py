from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # hashmap = {}
        # for num in arr:
        #     hashmap[num] = hashmap.get(num, 0) + 1
        # return len(hashmap) == len(set(hashmap.values()))
        
        freq_count = Counter(arr)
        return len(freq_count.values()) == len(set(freq_count.values()))

example = Solution()
print(example.uniqueOccurrences([1,2]))
        

