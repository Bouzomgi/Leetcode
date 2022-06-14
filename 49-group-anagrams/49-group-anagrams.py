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
                
        
        output = []
        counterList = []
        for elem in strs:
            counter = countLetters(elem)
            
            i = 0
            while i < len(counterList):
                if counter == counterList[i]:
                    output[i].append(elem)
                    break
                i += 1
            
            if i == len(counterList):
                output.append([elem])
                counterList.append(counter)
                
        return output

            

                
                
        