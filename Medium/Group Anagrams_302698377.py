class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=collections.defaultdict(list)
        for i in strs:
            a[tuple(sorted(i))].append(i)
        return a.values()
        
        
        
