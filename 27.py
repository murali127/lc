class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # Tracks the count of elements not equal to val
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move elements not equal to val to the front
                k += 1
        
        return k
