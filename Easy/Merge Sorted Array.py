def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #for i in range(nums1):
         #   if nums1[i] == 0:
         #       nums[i] = None
        
        iA = m-1
        iB = n-1
        iM = m+n-1
        
        while iB >= 0:
            if iA >= 0 and nums1[iA] > nums2[iB]:
                nums1[iM] = nums1[iA]
                iA-=1
            else:
                nums1[iM] = nums2[iB]
                iB-=1
            iM-=1