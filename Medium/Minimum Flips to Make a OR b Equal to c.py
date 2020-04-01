def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a or b or c:
            if (a&1) | (b&1) != c&1:
                if c&1:
                    count+=1
                else:
                    count+= (a&1)+(b&1)
            a,b,c=a>>1,b>>1,c>>1
        return count