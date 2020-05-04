class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp
        # buy[i] represent max profit when at day i, we buy or wait
        # sell[i] represent max profit when at day i, we sell or wait
        
        if len(prices) < 2:
            return 0

        # initialize two arrays
        buy, sell = [0]*len(prices), [0]*len(prices)
        buy[0] = -prices[0]
        sell[0] = 0
        buy[1] = max(buy[0], -prices[1])
        sell[1] = max(sell[0], prices[1] - prices[0])
        
        for i in range(2, len(prices)):
            # if at day i, buy can be more profit, then buy (can only buy when there is a cooldown gap), else wait
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])
            # at day i, sell can be more profit, then sell, else wait
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
        
        return max(buy[-1], sell[-1])
                
        
                
            
            
            
        