class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result=[]
        if not matrix:
            return []
        if len(matrix[0])==1:
            for i in range(len(matrix)):
                result.append(matrix[i][0])
        else:
            while matrix:
                result+=matrix.pop(0)# first line
                if matrix and matrix[0]:
                    for i in range(len(matrix)):
                        result.append(matrix[i].pop())
                if matrix:
                    result+=matrix.pop()[::-1]
                if matrix and matrix[0]:
                    for i in matrix[::-1]:
                        result.append(i.pop(0))
        return result
            
