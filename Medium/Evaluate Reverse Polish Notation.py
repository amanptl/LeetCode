def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                stack.append(-stack.pop() + stack.pop())
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                if a != 0:
                    stack.append(int(b / a))
            else:
                stack.append(int(token))
        return stack.pop()