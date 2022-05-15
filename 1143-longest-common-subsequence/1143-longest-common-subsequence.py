class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        #First attempt
#         def rec(text1, text2):
#             if not text1 or not text2:
#                 return 0
#             elif text1[0] == text2[0]:
#                 return 1 + rec(text1[1:], text2[1:])
#             else:
#                 return max(rec(text1[1:], text2), rec(text1, text2[1:]))
         
#         return rec(text1, text2)
    
        #Second attempt
        cache = {}
        def rec(i, j):
            if i == -1 or j == -1:
                return 0
            elif (i, j) in cache:
                return cache[(i, j)]
            elif text1[i] == text2[j]:
                return 1 + rec(i-1, j-1)
            else:
                cache[(i, j)] = max(rec(i-1, j), rec(i, j-1))
                return cache[(i, j)]
         
        return rec(len(text1)-1, len(text2)-1)