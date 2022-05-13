class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #brute force
        # maxVal = nums[0]
        # for i in range(len(nums)):
        #     arraySum = 0
        #     for j in range(i, len(nums)):
        #         arraySum += nums[j]
        #         if arraySum > maxVal:
        #             maxVal = arraySum
        # return maxVal
        
        
        #naive recursive solution
#         if not nums:
#             return 0
#         return max(nums[0] + self.maxSubArray(nums[1:]), self.maxSubArray(nums[1:]))
    
        #memoization
        #We have to keep track of a max value thru the process of finding the max subarray
        #Tricky to do with recursion, so recursive memoization is not a good technique
#         cache = {}
#         cache[0] = nums[0]
#         global maxSum
#         maxSum = cache[0]
#         def memo(i):
#             if i in cache:
#                 return cache[i]
#             cache[i] = max(nums[i] + memo(i-1), nums[i])
#             global maxSum
#             if cache[i] > maxSum: 
#                 maxSum = cache[i]
#             return cache[i]
    
#         memo(len(nums)-1)
#         return maxSum
    
    
        #tabulation
#         if len(nums) == 1: 
#             return nums[0]
        
#         tab = [0] * len(nums)
#         tab[0] = nums[0]
#         maxSum = nums[0]
#         for i in range(1, len(nums)):
#             tab[i] = max(nums[i], nums[i]+tab[i-1])
#             if tab[i] > maxSum:
#                 maxSum = tab[i]
#         return maxSum
    
        #reduced tab (since we are only using our previous computation in our table to 
        #generate the next computation, we do not need to store these computations beyond 
        #the recurrance relationship)
        maxVal, currMax = nums[0], nums[0]
        for i in range(1, len(nums)):
            currMax = max(currMax + nums[i], nums[i])
            if currMax > maxVal:
                maxVal = currMax
        return maxVal
            