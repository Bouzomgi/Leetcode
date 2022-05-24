
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         store = {}
#         i = 0
#         maxLen = 0
#         currLen = 0
#         while i < len(s):
#             if s[i] not in store:
#                 store[s[i]] = i
#                 currLen += 1
#                 maxLen = max(maxLen, currLen)
#                 i += 1
#             else:
#                 i = store[s[i]] + 1
#                 store = {}
#                 currLen = 0
                
#         return maxLen
                
        
        #second approach
        store = {}
        maxLen = 0
        start = 0
        for i in range(len(s)):
            
            if s[i] in store:
                start = max(store[s[i]], start)
                
            maxLen = max(i - start + 1, maxLen)
            store[s[i]] = i + 1
            
        return maxLen
                
            
            
            