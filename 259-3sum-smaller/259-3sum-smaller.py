class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        #Brute force
        # total = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             x, y, z = nums[i], nums[j], nums[k]
        #             if (x + y + z < target):
        #                 total += 1
        # return total
        
        
        #Runtime: O(n*n*log(n))
#         def twoSumSmaller(start, target):
#             l, r = start, len(nums) - 1
#             while l <= r:
#                 mid = (l + r) // 2
#                 if nums[mid] < target:
#                     l = mid + 1
#                 elif nums[mid] >= target:
#                     r = mid - 1
#             return l - start
        
#         total = 0
#         nums.sort()
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 twoSumTarget = target - nums[i] - nums[j]
#                 total += twoSumSmaller(j+1, twoSumTarget)
        
#         return total


        #Runtime: O(n^2)
        def twoSumSmaller(start, target):
            total = 0
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] >= target:
                    r -= 1
                else:
                    total += (r-l)
                    l += 1

            return total
        
        total = 0
        nums.sort()
        for i in range(len(nums)-2):
            print(i)
            twoSumTarget = target - nums[i]
            total += twoSumSmaller(i+1, twoSumTarget)
        
        return total
    
    
    [-9, -5, -1, 0, 4, 10, 16]
    
    
    12
    
    
                
        