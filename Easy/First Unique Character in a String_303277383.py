class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = collections.defaultdict(int)
        for i in s:
            a[i]+=1
        for i,x in enumerate(s):
            if a[x]==1:
                return i
        return -1
        
