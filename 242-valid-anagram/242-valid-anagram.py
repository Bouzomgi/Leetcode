class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Runtime: O(n)
        #Space: O(n)
#         counter = {}
#         for i in s:
#             if i not in counter:
#                 counter[i] = 1
#             else:
#                 counter[i] += 1
                
#         for i in t:
#             if i not in counter:
#                 return False
#             elif counter[i] == 1:
#                 del counter[i]
#             else:
#                 counter[i] -= 1
            
#         if counter:
#             return False
#         return True

        #Runtime: O(n)
        #Space: 1
        counter = [0]*26
        for i in s:
            counter[ord(i)%26] += 1
                
        for i in t:
            counter[ord(i)%26] -= 1
            
        for i in counter:
            if i != 0:
                return False
            
        return True