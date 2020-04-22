class NumArray:
    cache = []
    def __init__(self, nums: List[int]):
        self.cache = [0 for _ in range(len(nums)+1)]
        for i in range(len(nums)):
            self.cache[i+1] = self.cache[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.cache[j+1] - self.cache[i] 