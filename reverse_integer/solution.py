class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign=-1 
        if x<0:
            sign=-1
        else:
            sign=1
        x*=sign
        if x==0:
            return 0
        else:
            reverse_int=int(''.join(reversed(str(x))))
            if reverse_int<-2**31 or reverse_int>(2**31)-1:
                return 0
            else:
                return sign*reverse_int
