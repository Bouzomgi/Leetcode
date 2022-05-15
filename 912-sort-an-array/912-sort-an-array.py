class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        #Sorts two sorted lists
        def merge(l1, l2):
            final = []

            while l1 and l2:
                if l1[0] < l2[0]:
                    final.append(l1.pop(0))
                else:
                    final.append(l2.pop(0))
            while l1:
                final.append(l1.pop(0))
            while l2:
                final.append(l2.pop(0))
            
            return final
        
        def mergeSort(nums):
            if len(nums) >= 2:
                mid = len(nums) // 2
                left = mergeSort(nums[:mid])
                right = mergeSort(nums[mid:])
                return merge(left, right)
            return nums
        
        return mergeSort(nums)