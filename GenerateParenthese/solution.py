class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(current,left,right,result=[]):
            if left>0:
                generate(current+"(",left-1,right)
            if left<right: 
                generate(current+")",left,right-1)
            if not right:    result +=current ,
            return result
        return generate("",n,n)
