def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s,[],res)
        return res
    
    def isPal(self,string):
        return string == string[::-1]
    
    def dfs(self,s,path,res):
        if not s:
            res.append(path[:])
            return
        for i in range(1,len(s)+1):
            if self.isPal(s[:i]):
                path.append(s[:i])
                self.dfs(s[i:],path,res)
                path.pop()