# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        factor = 1
        while l1 or l2:
            if l1:
                total += (l1.val * factor)
                l1 = l1.next
            if l2:
                total += (l2.val * factor)
                l2 = l2.next
            factor *= 10
        
        sumLLHead = ListNode()
        sumLL = sumLLHead
        sumLL.val = total % 10
        total = total // 10 
        
        while total:
            sumLL.next = ListNode()
            sumLL = sumLL.next
            sumLL.val = total % 10
            total = total // 10
            
        return sumLLHead

