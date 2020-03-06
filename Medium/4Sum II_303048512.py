class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        a=collections.defaultdict(list)
        b=collections.defaultdict(list)
        c=0
        for i,x in enumerate(A):
            for j,y in enumerate(B):
                    a[x+y].append([i,j])
        for i,x in enumerate(C):
            for j,y in enumerate(D):
                    b[x+y].append([i,j])
        
        for i in a:
            if -1*i in b:
                c+=len(a[i])*len(b[-1*i])
                
        return c
                
        
