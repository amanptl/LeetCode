class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        a = []
        for i in matrix:
            for j in i:
                a.append(j)
        return sorted(a)[k-1]
