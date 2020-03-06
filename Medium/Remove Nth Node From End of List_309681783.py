# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        d = ListNode(0)
        d.next = head
        p1 = d
        p2 = d
        for i in range(n+1):
            p1 = p1.next
        while p1:
            p1 = p1.next
            p2 = p2.next
        print(p2.val)
        p2.next = p2.next.next
        return d.next
        
