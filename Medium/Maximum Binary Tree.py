def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        ind = 0
        m = float('-inf')
        for i in range(len(nums)):
            if nums[i] > m:
                m = nums[i]
                ind = i
        root = TreeNode(m)
        root.left = self.constructMaximumBinaryTree(nums[:ind])
        root.right = self.constructMaximumBinaryTree(nums[ind+1:])
        return root