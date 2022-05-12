class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 2
        lo, hi = 0, len(nums)
        
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return -1