class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            x=1/x
            n=-n
        if n==0:
            return 1
        result=1
        while n>0:
            if n&1!=0:
                result*=x
            x*=x
            n>>=1
        return result
