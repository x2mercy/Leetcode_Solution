class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)//2):
            temp=matrix[i]
            matrix[i]=matrix[len(matrix)-i-1]
            matrix[len(matrix)-i-1]=temp
        for i in range(len(matrix)):
            for j in range(i,len(matrix[i])):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
