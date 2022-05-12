class Solution:
    def climbStairs(self, n: int, memo={}) -> int:
        
        #naive recursive approach
        # if n <= 2:
        #     return n
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    
        #memoization (top down)
        # cache = {}
        # cache[1] = 1
        # cache[2] = 2
        # def memo(i):
        #     if i in cache:
        #         return cache[i]
        #     cache[i] = self.climbStairs(i - 1) + self.climbStairs(i - 2)
        #     return cache[i]
        if n <= 1:
            return 1
        if n in memo:
            return memo[n]
        memo[n] =  self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)
        return memo[n]
        
        
        
