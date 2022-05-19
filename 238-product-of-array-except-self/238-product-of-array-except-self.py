class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
#         #brute force
#         products = [1 for _ in range(len(nums))]
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if i != j:
#                     products[i] *= nums[j]
                    
#         return products
    
#         #O(n) w/o using division
#         forward = [1 for _ in range(len(nums))]
#         backward = [1 for _ in range(len(nums))]

#         prev = 1
#         for i in range(1, len(nums)):
#             forward[i] *= nums[i-1] * forward[i-1]
            
#             j = len(nums) - i - 1
#             backward[j] *= nums[j+1] * backward[j+1]
            
#         for i in range(len(forward)):
#             forward[i] *= backward[i]
        
#         return forward

        #O(n) w/o using division using O(1) space
        storeForward = 1
        final = [1 for _ in range(len(nums))]
        
        for i in range(1, len(nums)):
            final[i] *= nums[i-1] * final[i-1]            
        
        print(final)
        backwards = 1
        for i in range(1, len(nums)):
            j = len(nums) - i - 1
            backwards *= nums[j+1]
            final[j] *= backwards
            
        return final
            
        
    
    