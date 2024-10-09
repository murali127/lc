class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        filtered = ''
        for char in s:
            if char.isalnum():
                filtered += char.lower()
        return filtered == filtered[::-1]