class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #naive recursive solution
#         if not nums:
#             return 0
#         return max(nums[0] + self.maxSubArray(nums[1:]), self.maxSubArray(nums[1:]))
    
        #memoization
        #We have to keep track of a max value thru the process of finding the max subarray
        #Tricky to do with recursion, so recursive memoization is not a good technique
        cache = {}
        cache[0] = nums[0]
        global maxVal
        maxVal = cache[0]
        def memo(i):
            if i in cache:
                return cache[i]
            cache[i] = max(nums[i] + memo(i-1), nums[i])
            global maxVal
            if cache[i] > maxVal: 
                maxVal = cache[i]
            return cache[i]
    
        memo(len(nums)-1)
        return maxVal
            