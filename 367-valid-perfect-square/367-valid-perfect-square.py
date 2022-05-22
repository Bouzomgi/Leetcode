class Solution:
    def isPerfectSquare(self, num: int) -> bool:
#         #brute force
#         if num == 1: 
#             return True
        
#         for i in range(2, num//2 + 1):
#             if i * i == num:
#                 return True
#         return False

        #binary search
        if num == 1: 
            return True
    
        l, r = 1, num//2 + 1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                r = mid - 1
            else: 
                l = mid + 1
        return False