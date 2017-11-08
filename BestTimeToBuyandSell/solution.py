class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_diff=0
        min_price=max(prices)
        for i in range(0,len(prices)):
            min_price=min(min_price,prices[i])
            max_diff=max(max_diff,prices[i]-min_price)
            
        return max_diff
