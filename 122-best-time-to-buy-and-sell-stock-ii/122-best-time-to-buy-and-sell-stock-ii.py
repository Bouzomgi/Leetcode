class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #first attempt solution (not looking at answer)
        lastdip = prices[0]
        lastpeak = 0 #we cannot sell on the first day so we do not treat it as a peak
        prevstock = 0
        maxprof = 0
        #want to buy on the dips and sell on the peaks
        for i in prices[1:] + [0]:  #add a 0 at the end to add a peak on the last day
            lastpeak = max(lastpeak, i)
            
            #local max
            if prevstock > i:
                maxprof += (lastpeak - lastdip)
                lastdip, lastpeak = i, i
                
            else: 
                lastdip = min(lastdip, i)
            
            prevstock = i

        return maxprof
            
                