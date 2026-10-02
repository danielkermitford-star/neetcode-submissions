class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for p in prices[1:]:
            max_profit = max(max_profit, p - min_price)
            min_price = min(min_price, p)
        return max_profit

        