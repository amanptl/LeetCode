def minAddToMakeValid(self, S: str) -> int:
        stack = []
        res = []
        for i in range(len(S)):
            c = S[i]
            if c == '(':
                stack.append(c)
            else:
                if stack:
                    if stack.pop() == '(':
                        continue
                    else:
                        stack.append('(')
                        stack.append(c)
                else:
                    stack.append(c)
                    
        return len(stack)