# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-9-3 上午8:26

"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if len(prices) == 1:
            return profit
        for i in range(len(prices) - 1):
            if prices[i] <= prices[i + 1]:
                profit += (prices[i + 1] - prices[i])
        return profit


if __name__ == '__main__':
    # prices = [7, 1, 5, 3, 6, 4]
    # prices = [1, 2, 3, 4, 5]
    prices = [7, 6, 4, 3, 1]
    profit = Solution().maxProfit(prices)
    print(profit)
