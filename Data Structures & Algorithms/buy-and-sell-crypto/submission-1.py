class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mn = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[mn]:
                mn = i
            
            else:
                profit = max(profit, prices[i]-prices[mn])
        return profit
