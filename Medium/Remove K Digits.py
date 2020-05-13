def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        
        for _ in range(k):
            i = 0
            while i < len(num) - 1 and num[i] <= num[i+1]:
                i += 1
            num = num[:i] + num[i+1:]
        
        return self.removeZeros(num)
    
    def removeZeros(self, num):
        i = 0
        
        while i < len(num) and num[i] == '0':
            i += 1
        
        if i == len(num):
            return '0'
        
        return num[i:]