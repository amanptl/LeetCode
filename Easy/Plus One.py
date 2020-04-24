def plusOne(self, nums: List[int]) -> List[int]:
        carry = 1
        for i in range(len(nums)-1,-1,-1):
            nums[i] += carry
            if nums[i] > 9:
                nums[i] %= 10
                carry = 1
            else:
                carry = 0
        
        if carry == 0:
            return nums
        nums.insert(0,carry)
        return nums