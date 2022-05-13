class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #naive recursion
#         def memo(i):
#             if i == 0:
#                 return nums[0]
#             elif i == 1:
#                 return max(nums[1], nums[0])
#             return max(nums[i] + memo(i-2), memo(i-1))
        
#         return memo(len(nums)-1)
    
        #memoization
#         if len(nums) == 1: 
#             return nums[0]
        
#         cache = {}
#         cache[0] = nums[0]
#         cache[1] = max(nums[1], nums[0])
#         def memo(i):
#             if i in cache:
#                 return cache[i]
#             cache[i] = max(nums[i] + memo(i-2), memo(i-1))
#             return cache[i]
        
#         return memo(len(nums)-1)

        #tabulation
        if len(nums) == 1:
            return nums[0]
        tab = [0] * len(nums)
        tab[0] = nums[0]
        tab[1] = max(nums[0], nums[1])
        for i in range(2, len(tab)):
            tab[i] = max(nums[i] + tab[i-2], tab[i-1])
        return tab[-1]
    
    