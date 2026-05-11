

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float("inf")
        maxgain = 0
        for price in prices:
            if price < lowest:
                lowest = price
            elif maxgain < price-lowest:
                maxgain = price-lowest  
        return maxgain        
            