class Solution:
    def longestPalindrome(self, s: str) -> str:

            if not s:
                return ""
            
            tab = [[False] * len(s) for _ in range(len(s))]
            
            longestP = s[0]
            
            for i in range(len(s)):
                tab[i][i] = True
            
            for i in range(len(s), -1, -1):
                for j in range(i+1, len(s)):
                    if s[i] == s[j]:
                        if (i == j - 1) or tab[i+1][j-1]:
                            tab[i][j] = True
                            if len(s[i:j+1]) > len(longestP):
                                longestP = s[i:j+1]
            
            return longestP