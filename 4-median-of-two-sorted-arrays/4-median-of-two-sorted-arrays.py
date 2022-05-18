class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        #First attempt: linear runtime
        #merge -> binary search

#         def merge(nums1, nums2):
            
#             final = [0 for _ in range(len(nums1)+len(nums2))]
#             i, j, k = 0, 0, 0
            
#             while i < len(nums1) and j < len(nums2):
#                 if nums1[i] < nums2[j]:
#                     final[k] = nums1[i]
#                     i+=1
#                 else:
#                     final[k] = nums2[j]
#                     j+=1
#                 k+=1

#             while i < len(nums1):
#                 final[k] = nums1[i]
#                 i+=1
#                 k+=1
                    
#             while j < len(nums2):
#                 final[k] = nums2[j]
#                 j+=1
#                 k+=1
                
#             return final
        
#         final = merge(nums1, nums2)
            
#         mid = len(final) // 2
#         if len(final) % 2:
#             return final[mid]
#         return (final[mid] + final[mid - 1]) / 2

        #Binary Search
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A, B = B, A
        
        totalLength = len(A) + len(B)
        half = totalLength // 2
        l, r = 0, len(A)-1
        
        while True:
            AmidIndex = (r+l) // 2
            BmidIndex = half - 2 - AmidIndex
            
            Amid = A[AmidIndex] if AmidIndex >= 0 else -math.inf
            Aright = A[AmidIndex + 1] if AmidIndex + 1 < len(A) else math.inf
            Bmid = B[BmidIndex] if BmidIndex >= 0 else -math.inf
            Bright = B[BmidIndex + 1] if BmidIndex + 1 < len(B) else math.inf

            print(AmidIndex, BmidIndex)

            
            if Bmid > Aright:
                l = AmidIndex + 1
                
            elif Amid > Bright:
                r = AmidIndex - 1
                
            else:
                if totalLength % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Amid, Bmid) + min(Aright, Bright)) / 2
            
        
        
        
        
        
        
