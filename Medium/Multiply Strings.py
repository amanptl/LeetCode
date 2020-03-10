def multiply(self, num1: str, num2: str) -> str:
        def to_int(s):
            val = 0
            i = 0
            for e in s[::-1]:
                if i > 0:
                    val += (ord(e)-48) * (10**i)
                else:
                    val += (ord(e)-48)
                i+=1
            return val
        
        def to_str(n):
            s = []
            if n == 0:
                return '0'
            while n!=0:
                s.append(chr(ord('0') + n % 10))
                n //= 10
            return ''.join(reversed(s))
        
        ans = to_int(num1) * to_int(num2)
        #print(to_int(num1),to_int(num2),ans)
        return (to_str(ans))