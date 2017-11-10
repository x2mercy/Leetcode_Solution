class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<5:
            return 0
        result=n/5+self.trailingZeroes(n/5)
        return result
