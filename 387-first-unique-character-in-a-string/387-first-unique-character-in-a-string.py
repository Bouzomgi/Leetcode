class Solution:
    def firstUniqChar(self, s: str) -> int:
        charSet = dict()
        for char in s:
            if char not in charSet:
                charSet[char] = 1
            else:
                charSet[char] += 1
                
        for i in range(len(s)):
            if charSet[s[i]] == 1:
                return i
            
        return -1
            