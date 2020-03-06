class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        sol = []
        temp = []
        
        pair = sorted(list(zip(groupSizes, range(len(groupSizes)))))

        for size, pid in pair:
            if len(temp) < size:
                temp.append(pid)
            if len(temp) == size:
                sol.append(temp)
                temp = []
        return sol
                   
