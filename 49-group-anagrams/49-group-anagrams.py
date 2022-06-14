class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def countLetters(x):
            strCounter = {}
            for char in x:
                if char not in strCounter:
                    strCounter[char] = 1
                else:
                    strCounter[char] += 1
                    
            return strCounter
                
        #Runtime: O(n^2)
#         output = []
#         counterList = []
#         for elem in strs:
#             counter = countLetters(elem)
            
#             i = 0
#             while i < len(counterList):
#                 if counter == counterList[i]:
#                     output[i].append(elem)
#                     break
#                 i += 1
            
#             if i == len(counterList):
#                 output.append([elem])
#                 counterList.append(counter)
                
#         return output
    
    
        #Runtime: O(n)
        hashList = []
        hashDict = {}
        output = []

        for elem in strs:
            sortedElem = sorted(elem)
            hashedElem = hash(tuple(sortedElem))
            hashList.append(hashedElem)
        
        x = 0
        for i in range(len(strs)):
            if hashList[i] in hashDict:
                anagramIndex = hashDict[hashList[i]]
                output[anagramIndex].append(strs[i])
                
            else:
                hashDict[hashList[i]] = x
                x += 1
                output.append([strs[i]])
            

        return output
                
        