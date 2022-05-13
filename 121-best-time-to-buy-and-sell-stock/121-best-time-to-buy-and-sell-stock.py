class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force
#         maxprof = 0
#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                 maxprof = max(maxprof, prices[j]-prices[i])
                
#         return maxprof
            
        #memoization is a poor choice: the recurrance relationship here will be to 
        #determine the best time to sell a single stock, not a specific profit. We will
        #need to store that max profit in a varible, which will probably have to be declared as global
    
        #tabulation/Kadane's algorithm
        maxprof = 0
        minstock = math.inf
        for i in prices:
            minstock = min(minstock, i)
            maxprof = max(maxprof, i-minstock)
        return max(maxprof, 0)
        
