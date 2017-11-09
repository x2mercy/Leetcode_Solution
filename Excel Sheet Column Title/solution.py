  class Solution(object):
    def convertToTitle(self,n):
        if n==0:
            return ""
        alpha={}
        result=[]
        for i in range(1,27):
            alpha[i]=chr(i+64)
        while n>0:
            result.append(alpha[(n-1)%26+1])
            n=(n-1)//26
        result.reverse()
        return ''.join(result)
        
