class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = {}
        r = []
        sol = []
        temp = []
        for i,x in enumerate(S):
            if x not in d:
                d[x] = [i,None]
        
        for i in range(len(S)-1,-1,-1):
            if d.get(S[i])[1] == None:
                d.get(S[i])[1] = i
        
        sorted(d, key=lambda x: d.get(x)[0])
        
        #for val in d.values():
            #r.append(val)
        r = list(d.values())
        i=0
        temp = r[0]
        for i in range(1,len(r)):
            if temp[1] >= r[i][0]:
                temp = [temp[0],max(temp[1],r[i][1])]
            else:
                sol.append(temp[1]-temp[0]+1)
                temp = r[i]
        sol.append(temp[1]-temp[0]+1)
        return sol
        
                
    
                
                
