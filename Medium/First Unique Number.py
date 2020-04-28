class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = []
        self.lookup = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while len(self.q) > 0 and self.lookup[self.q[0]] > 1:
            self.q.pop(0)
        if len(self.q) == 0:
            return -1
        else:
            return self.q[0]

    def add(self, value: int) -> None:
        if value not in self.lookup:
            self.lookup[value] = 1
            self.q.append(value)
        else:
            self.lookup[value] += 1