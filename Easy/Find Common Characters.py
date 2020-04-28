def commonChars(self, A: List[str]) -> List[str]:
        check = list(A[0])
        
        for word in A[1:]:
            chck = []
            for c in word:
                if c in check:
                    chck.append(c)
                    check.remove(c)
            check = chck
        
        return check