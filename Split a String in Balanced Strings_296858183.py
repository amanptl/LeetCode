class Solution:
    def balancedStringSplit(self, s: str) -> int:
        total = 0
        stack_l = []
        stack_r = []
        
        for i in range(len(s)):
            if s[i] == 'L':
                stack_l.append(s[i])
            else:
                stack_r.append(s[i])
            if(len(stack_l)==len(stack_r)):
                stack_l = []
                stack_r = []
                total +=1
        
        return total
