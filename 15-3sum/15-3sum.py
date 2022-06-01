class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Brute force
#         total = []
#         onlyOne = set()
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(j+1, len(nums)):
#                     x, y, z = nums[i], nums[j], nums[k]
#                     if x+y+z == 0:
#                         curr = tuple(sorted([x, y, z]))
#                         if curr not in onlyOne:
#                             total.append([x, y, z])
#                             onlyOne.add(curr)
                        
#         return total
    
    
#         #Runtime: O(n^2)
#         total = []
#         tracker = {}
#         onlyOne = set()
        
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                     x, y = nums[i], nums[j]
#                     z = -(x + y)
#                     if z not in tracker:
#                         tracker[z] = [i, j]
                        
#         for k in range(len(nums)):
#             z = nums[k]
#             if z in tracker and k not in tracker[z]:
#                 x, y = nums[tracker[z][0]], nums[tracker[z][1]]
#                 combo = tuple(sorted([x, y, z]))
#                 if combo not in onlyOne:
#                     total.append([x, y, z])
#                     onlyOne.add(combo)
                        
#         return total

        def twoSum2(start, target, res):
            i, j = start, len(nums)-1
            while i < j:
                x, y = nums[i], nums[j]
                if x + y == target:
                    res.append([-target, x, y])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                elif x + y < target:
                    i += 1
                elif x + y > target:
                    j -= 1

        final = []
        nums.sort()
        for k in range(len(nums)):
            val = nums[k]
            if k == 0 or val != nums[k-1]:
                twoSum2(k+1, -val, final)
        return final

    
