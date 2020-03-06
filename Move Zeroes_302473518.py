class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[z] = nums[z],nums[i]
                z+=1
                
        
