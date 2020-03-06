# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        if head:
            odd = head
            even = evenHead = odd.next
            while even and even.next:
                odd.next = odd = even.next
                even.next = even = odd.next
            odd.next = evenHead
        return head
        
