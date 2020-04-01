def sortByBits(self, arr: List[int]) -> List[int]:
        '''import collections
        def count(n):
            count = 0
            while n != 0:
                if n & 1 == 1:
                    count += 1
                n >>= 1
            return count
        
        d = collections.defaultdict(list)
        res = []
        
        for num in arr:
            d[count(num)].append(num)
            
        for i in sorted(d):
            for n in sorted(d[i]):
                res.append(n)
                
        return res
        '''
        
        arr.sort(key=lambda x: [bin(x).count('1'), x])
        return arr