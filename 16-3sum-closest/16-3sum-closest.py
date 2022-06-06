class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #brute force
        # closest = math.inf
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             x, y, z = nums[i], nums[j], nums[k]
        #             closestDif = abs(closest-target)
        #             currDif = abs(x+y+z-target)
        #             if currDif < closestDif:
        #                 closest = x+y+z
        # return closest
        
        def twoSumClosest(start, z):
            closest = math.inf
            l, r = start, len(nums) - 1
            while l < r:
                x, y = nums[l], nums[r]
                
                if abs(x+y+z - target) < abs(closest - target):
                    closest = x+y+z
                    
                if abs(z+nums[l+1]+y - target) < abs(z+x+nums[r-1] - target):
                    l += 1
                else:
                    r -= 1
                    
            return closest
                
    
        #Runtime: O(n^2)
        closest = math.inf
        nums.sort()
        
        for i in range(len(nums)-2):    
            currClosest = twoSumClosest(i+1, nums[i])
            if abs(currClosest - target) < abs(closest - target):
                closest = currClosest
            
        return closest        

    
                    