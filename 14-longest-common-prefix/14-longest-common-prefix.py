class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        maxPre = ''
        shortestWord = strs[0]
        for word in strs:
            if len(word) < len(shortestWord):
                shortestWord = word
        
        for i in range(len(shortestWord)):
            for word in strs:
                if word[i] != shortestWord[i]:
                    return maxPre
            maxPre += shortestWord[i]
            
        return maxPre
                