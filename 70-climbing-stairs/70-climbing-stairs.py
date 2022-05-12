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
#         @lru_cache
#         def memo(i):
#             if i <= 2:
#                 return i
#             return memo(i-1) + memo(i-2)
        
#         return memo(n)

#tabulation
        if n<=2:
            return n
        
        tab = [0] * (n+1) 
        tab[1] = 1
        tab[2] = 2
        for i in range(3, n+1):
            tab[i] = tab[i-1] + tab[i-2]
            
        return tab[-1]
        
    