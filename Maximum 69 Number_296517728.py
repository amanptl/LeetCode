class Solution:
    def maximum69Number (self, num: int) -> int:
        n = str(num)
        for i in range(len(n)):
            if(n[i]!= '9'):
                n = n[:i]+'9'+n[i+1:]
                return int(n)
        return num
