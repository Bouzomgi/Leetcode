class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #brute force
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i]+numbers[j]==target:
        #             return [i+1, j+1]
        # return -1
        
        i = 0
        j = len(numbers)-1
        
        while i < j:
            l, r = numbers[i], numbers[j]
            if l + r == target:
                return [i+1, j+1]
            elif l + r < target:
                i += 1
            elif l + r > target:
                j -= 1
            
        return -1
                        
        
        