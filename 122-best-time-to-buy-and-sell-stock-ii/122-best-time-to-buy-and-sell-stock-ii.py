class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lastdip = prices[0]
        lastpeak = 0
        prevstock = 0
        maxprof = 0
        #want to buy on the dips and sell on the peaks
        for i in prices[1:] + [0]:
            lastpeak = max(lastpeak, i)
            
            #local max
            if prevstock > i:
                maxprof += (lastpeak - lastdip)
                lastdip, lastpeak = i, i
                
            else: 
                lastdip = min(lastdip, i)
            
            prevstock = i

        return maxprof
            
                