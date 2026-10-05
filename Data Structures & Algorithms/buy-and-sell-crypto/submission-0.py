class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = ""
        highest = ""
        # x-y = profit, where y>x
        for x in prices:
            i = prices.index(x)
            size = len(prices)
            for y in range(i+1,size):
                delta = prices[y]-x
                if delta > profit: profit = delta
        return profit