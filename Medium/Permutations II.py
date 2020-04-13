def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        import itertools
        return list(set(itertools.permutations(nums)))