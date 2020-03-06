class Solution:
    maxLen = 0

    def maxLength(self, arr):  # 1
        def hasDuplicates(s):
            return len(s) > len(set(s))

        def backtrack(index, s):
            self.maxLen = max(len(s), self.maxLen)

            if index == len(arr):
                return

            for i in range(index, len(arr)):
                if not hasDuplicates(s + arr[i]):
                    backtrack(i + 1, s + arr[i])

        if not arr:
            return 0
        self.maxLen = 0
        backtrack(0, "")
        return self.maxLen
