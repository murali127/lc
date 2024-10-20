class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 | n==1 :
            return 1
        a,b=1,1
        for i in range(2,n+1):
            c=a+b
            a,b=b,c
        return b
