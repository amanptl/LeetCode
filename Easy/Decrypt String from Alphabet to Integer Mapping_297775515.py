class Solution:
    def freqAlphabets(self, s: str) -> str:
        from collections import deque
        stack = deque(s)
        ans = []
        sol = ""
        
        while len(stack)!=0:
            c = stack.pop()
            if c == '#':
                t2 = str(stack.pop())
                t1 = str(stack.pop())
                ans.append(t1+t2)
            else:
                ans.append(c)
                
        ans.reverse()
        for i in ans:
            sol+=chr(96+int(i))
        
        return sol
               
