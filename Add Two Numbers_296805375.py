# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack = []
        t1 = ''
        t2 = ''
        ln = ListNode(0)
        
        def get_value(node):
            stack.append(node.val)
            if(node.next!=None):
                get_value(node.next)
        
        def put_value(node, s):
            if(len(s)==0):
                node.next=None
            else:
                node.val = s.pop()
                if(len(s)==0):
                    return ln
                node.next = ListNode(0)
                put_value(node.next,s)
                
            
        get_value(l1)
        for i in range(len(stack)):
            t1+=str(stack.pop())
        get_value(l2)
        for i in range(len(stack)):
            t2+=str(stack.pop())
        
        total = str(int(t1)+int(t2))
        for i in range(len(total)):
            stack.append(total[i])
        
        print(stack)
        put_value(ln,stack)
        return ln
        
            
