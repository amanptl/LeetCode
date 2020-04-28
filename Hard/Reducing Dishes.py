def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        curr = 0
        cumm = 0
        ans = 0
        for i in range(len(satisfaction)-1,-1,-1):
            curr += cumm + satisfaction[i]
            cumm += satisfaction[i]
            ans = max(ans,curr)
        return ans