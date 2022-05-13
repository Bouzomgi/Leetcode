class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for elem in nums:
            if elem in numSet:
                return True
            numSet.add(elem)
        return False