class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #naive recursion
        @cache
        def memo(i):
            if i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[1], nums[0])
            return max(nums[i] + memo(i-2), memo(i-1))
        
        return memo(len(nums)-1)