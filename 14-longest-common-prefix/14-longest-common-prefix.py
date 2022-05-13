class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        #First approach
#         maxPre = ''
#         shortestWord = strs[0]
#         for word in strs:
#             if len(word) < len(shortestWord):
#                 shortestWord = word
        
#         for i in range(len(shortestWord)):
#             for word in strs:
#                 if word[i] != shortestWord[i]:
#                     return maxPre
#             maxPre += shortestWord[i]
            
#         return maxPre
                
    
        #Second approach (vertical scanning)
        for i in range(len(strs[0])):
            for word in strs:
                if len(word) == i or word[i] != strs[0][i]: 
                    return strs[0][:i]
        return strs[0]