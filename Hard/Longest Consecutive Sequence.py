def longestConsecutive(self, nums: List[int]) -> int:
        m = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                curr_num = num
                curr = 1
                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr += 1
                m = max(m,curr)
        return m