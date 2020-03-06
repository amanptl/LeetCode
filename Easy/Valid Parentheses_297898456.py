class Solution:
    def isValid(self, s: str) -> bool:
        while len(s)>1:
            curr_size = len(s)
            if '[]' in s:
                s = s.replace('[]','')
            if '()' in s:
                s = s.replace('()','')
            if '{}' in s:
                s = s.replace('{}','')
            if curr_size == len(s):
                break

        if len(s)==0:
            return True
        else:
            return False
        
