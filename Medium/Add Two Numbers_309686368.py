# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        head = dummy
        carryover = 0
        while l1 or l2:
            
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
            
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0
            
            val = l1_val + l2_val + carryover
            carryover = 0
            if val > 9:
                carryover = val // 10
                val = val % 10
                
            head.next = ListNode(val)
            head = head.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carryover > 0:
            head.next = ListNode(carryover)
        
        return dummy.next
        
            
