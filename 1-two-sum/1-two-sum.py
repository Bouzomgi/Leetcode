class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
                
        #hash table
        store = {}
        for i in range(len(nums)):
            if nums[i] in store:
                return [i, store[nums[i]]]
            store[target - nums[i]] = i