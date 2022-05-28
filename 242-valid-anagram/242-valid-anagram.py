class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        for i in s:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1
                
        for i in t:
            if i not in counter:
                return False
            elif counter[i] == 1:
                del counter[i]
            else:
                counter[i] -= 1
            
        if counter:
            return False
        return True