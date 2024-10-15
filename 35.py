class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid  # Target found
            elif nums[mid] < target:
                left = mid + 1  # Target could be on the right side
            else:
                right = mid - 1  # Target could be on the left side
        
        return left 
        
