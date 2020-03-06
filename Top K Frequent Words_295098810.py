class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        temp = words.sort()
        temp = collections.Counter(words)
        top = temp.most_common(k)
        ans = dict(top).keys()
        return ans
