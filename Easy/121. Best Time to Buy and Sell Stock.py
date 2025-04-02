class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 1 # Left = Buy, Right = Sell
        maxP = 0 # default
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit) # Returns highest number
            else:
                l = r
            r += 1
        return maxP

# TC: O(N)
# SC: O(1)