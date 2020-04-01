def hasAlternatingBits(self, n: int) -> bool:
        s = bin(n)[2:]
        p = s[0]
        for i in s[1:]:
            if p == i:
                return False
            p = i
        return True