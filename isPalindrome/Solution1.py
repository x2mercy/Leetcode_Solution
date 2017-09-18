class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if x==0:
            return True
        else:
            reverse_int=int(''.join(reversed(str(x))))
        if reverse_int==x:
            return True
        else:
            return False
