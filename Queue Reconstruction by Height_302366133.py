class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = [[]]*len(people)
        people.sort(key=lambda x: (x[0],-x[1]))
        indices = [i for i in range(len(people))]
        for z,(x,y) in enumerate(people):
            i = indices.pop(y)
            ans[i] = people[z]
        return ans
        
