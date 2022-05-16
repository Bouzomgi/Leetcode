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
#         cache = {}
#         def memo(i, j):
#             if i == -1 or j == -1:
#                 return 0
#             elif (i, j) in cache:
#                 return cache[(i, j)]
#             elif text1[i] == text2[j]:
#                 return 1 + memo(i-1, j-1)
#             else:
#                 cache[(i, j)] = max(memo(i-1, j), memo(i, j-1))
#                 return cache[(i, j)]
         
#         return memo(len(text1)-1, len(text2)-1)
    
        #Tabulation
        tab = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        #Our table has an additional row and col of 0's, so the indexing will be different on the table + the strings

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    #Take diagonal square as in that problem, the current letter has not been used up
                    tab[i+1][j+1] = tab[i][j] + 1
                else:
                    tab[i+1][j+1] = max(tab[i][j+1], tab[i+1][j])
        return tab[-1][-1]
        