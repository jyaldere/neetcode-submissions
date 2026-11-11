class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, mini = 0, float('inf')

        for price in prices:
            mini = min(mini, price)
            profit = max(price - mini, profit)

        return profit