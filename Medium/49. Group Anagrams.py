from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = defaultdict(list)
        for s in strs:
            count = [0] * 26 # List to count each letter
            for c in s:
                count[ord(c) - ord("a")] += 1 # Determines where letter to add
            hashmap[tuple(count)].append(s) # Converts count list to tuple 
        return hashmap.values() 
        

# TC: O(M*N)
# SC: O(M*N)