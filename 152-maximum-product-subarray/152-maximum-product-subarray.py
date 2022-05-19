class Solution:
    def maxProduct(self, nums: List[int]) -> int:

#         #brute force
#         maxProd = -math.inf
#         for i in range(len(nums)):
#             currProd = 1
#             for j in range(i, len(nums)):
#                 currProd *= nums[j]
#                 maxProd = max(maxProd, currProd)

#         return maxProd
            
        #dp     
        minProdSoFar = 1
        maxProdSoFar = 1
        maxProd = -math.inf
        
        for num in nums:
            tempMax = max(num, maxProdSoFar * num, minProdSoFar * num)
            minProdSoFar = min(num, minProdSoFar * num, maxProdSoFar * num)
            maxProdSoFar = tempMax
            print(maxProdSoFar, minProdSoFar)
            maxProd = max(maxProd, maxProdSoFar)
            
        return maxProd

            
            
            
                
                