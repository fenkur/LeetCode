class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # If it's negative then it can't be a palindrome
        if x < 0:
            return False
        
        reverse = 0
        xcopy = x
        while xcopy != 0:
            digit = xcopy % 10 # Get's the last digit of the number
            reverse = reverse * 10 + digit #Shifts the number to the left and adds the new digit
            xcopy = xcopy / 10 # Removes the last digit
        
        return reverse == x #Checks and returns if the reverse is equal to input number

        # Time Complexity: O(Log10(x))
        # Space Complexity: O(1)

        # return str(x) == str(x)[::-1] alternate answer: TC: O(N) SC: O(N)


