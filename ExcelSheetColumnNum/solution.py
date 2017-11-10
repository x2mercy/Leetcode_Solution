class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        alpha={}
        result=0
        for i in range(1,27):
            alpha[chr(i+64)]=i
        s=s[::-1]
        for i in range(len(s)):
            result+=alpha[s[i]]*(26**i)
        return result
        
            
