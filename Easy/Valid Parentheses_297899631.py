class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        while len(s)>0:
            curr_size = len(s)
            if '[]' in s:
                s = s.replace('[]','')
            if '()' in s:
                s = s.replace('()','')
            if '{}' in s:
                s = s.replace('{}','')
            if curr_size == len(s):
                return False
        return True
        
