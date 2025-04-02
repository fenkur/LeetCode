
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # TC: O(N) SC: O(1)
        L = 0
        R = len(s) - 1
        while L < R:
            s[L], s[R] = s[R], s[L]
            l, r = l + 1, r - 1
        
        

        

        