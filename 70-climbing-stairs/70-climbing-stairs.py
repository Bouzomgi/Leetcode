class Solution:
    def climbStairs(self, n: int) -> int:
        
          #naive recursive approach
#         if n <= 2:
#             return n
#         return self.climbStairs(n-1) + self.climbStairs(n-2)
    
          #memoization
#         cache = {}
#         cache[1] = 1
#         cache[2] = 2
#         def memo(i):
#             if i in cache:
#                 return cache[i]
#             cache[i] = memo(i-1) + memo(i-2)
#             return cache[i]
        
#         return memo(n)

        #memoization using functools @cache
        @cache
        def memo(i):
            if i <= 2:
                return i
            return memo(i-1) + memo(i-2)
        
        return memo(n)
    