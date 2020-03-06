class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d=collections.defaultdict(int)
        a={}
        for i in arr:
            d[i]+=1
        for i in d.values():
            if i in a:
                return False
            a[i]=""
        return True
