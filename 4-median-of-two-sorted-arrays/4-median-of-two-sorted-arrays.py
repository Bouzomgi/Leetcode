class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        final = [0 for _ in range(len(nums1)+len(nums2))]
        i, j, k = 0, 0, 0
        
        #merge -> binary search
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                final[k] = nums1[i]
                i+=1
            else:
                final[k] = nums2[j]
                j+=1
            k+=1
                
        while i < len(nums1):
            final[k] = nums1[i]
            i+=1
            k+=1
        
        while j < len(nums2):
            final[k] = nums2[j]
            j+=1
            k+=1
            
        mid = len(final) // 2
        if len(final) % 2:
            return final[mid]
        return (final[mid] + final[mid - 1]) / 2
        