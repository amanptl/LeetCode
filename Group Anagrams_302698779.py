class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=collections.defaultdict(list)
        for i in strs:
            a[tuple(sorted(i))].append(i)
        output = []
        for key in a:
            output.append(a[key])
        return output
        
        
        
