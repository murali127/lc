class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<=1:
            return x
        a=0
        while (a+1)*(a+1)<=x:
            a+=1
        return a
