class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        # Traverse the digits from the end
        for i in range(n - 1, -1, -1):
            # If the current digit is less than 9, just increment it and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # Otherwise, set the current digit to 0 (carry over)
            digits[i] = 0
        
        # If all digits were 9, add a new leading 1
        return [1] + digits
