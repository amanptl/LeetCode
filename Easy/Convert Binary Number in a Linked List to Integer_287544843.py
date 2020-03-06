# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node = head
        v = str(node.val)
        while node.next is not None:
            node = node.next
            v = str(v) + str(node.val)
        return int(v, 2)
