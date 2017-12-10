class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result=[]
        left=n*n+1
        while left>1:
            left,right=left-len(result),left
            result=[range(left,right)]+zip(*result[::-1])
        return result 
        
        
        
        
