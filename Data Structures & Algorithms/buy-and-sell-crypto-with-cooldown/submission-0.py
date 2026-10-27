# https://neetcode.io/problems/buy-and-sell-crypto-with-cooldown/question?list=neetcode150
from cmath import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        CAN_BUY = 0
        JUST_SOLD = 1    # don't have it
        HAVE_IT = 2
        # three columns 0/1/2 for can_buy / just_sold / have_it
        max_profit = [[0 for _ in range(3)] for _ in range(length+1)]
        max_profit[0][JUST_SOLD] = max_profit[0][HAVE_IT] = -inf # must purchase the stock first
        for i in range(1,length+1):
            could_already_buy_it = max_profit[i-1][CAN_BUY]
            sold_it_last_time = max_profit[i-1][JUST_SOLD]          # at prices[i-2]
            bought_it = max_profit[i-1][CAN_BUY] - prices[i-1]      # just bought it at prices[i-1]
            had_it_already = max_profit[i-1][HAVE_IT]

            max_profit[i][CAN_BUY] = max(could_already_buy_it, sold_it_last_time)   # can buy next time, at prices[i]
            max_profit[i][JUST_SOLD] = max_profit[i-1][HAVE_IT] + prices[i-1]       # at prices[i-1]
            max_profit[i][HAVE_IT] = max(bought_it, had_it_already)

        return max(max_profit[-1][JUST_SOLD], max_profit[-1][CAN_BUY])

prices = [1,3,4,0,4]
prices = [1]
print(Solution().maxProfit(prices))