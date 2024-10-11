class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        pairs={'(':')','{':'}','[':']'}
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if not stack or pairs[stack.pop()]!=char:
                    return False
        return len(stack)==0

