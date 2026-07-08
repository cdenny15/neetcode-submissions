class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float('inf')
        max_profit = 0

        for price in prices:
            new = price - min_val
            if price < min_val:
                min_val = price
            elif new > max_profit:
                max_profit = new
            
        return max_profit


        