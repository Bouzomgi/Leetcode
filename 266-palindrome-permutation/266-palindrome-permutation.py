class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        letterCount = {}
        for letter in s:
            if letter not in letterCount:
                letterCount[letter] = 1
            else:
                letterCount[letter] += 1
            
        hasOddVals = False
        for i,j in letterCount.items():
            if j % 2 == 1:
                if hasOddVals == True:
                    return False
                hasOddVals = True
                
        return True