class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result=[[1],[1,1]]
        if rowIndex==0:
            return result[0]
        if rowIndex==1:
            return result[1]
        
        for i in range(2,rowIndex+1):
            nums=[]
            nums.append(1)
            while len(nums)<i:
                nums.append(result[i-1][len(nums)-1]+result[i-1][len(nums)])
            nums.append(1)
            result.append(nums)
        return result[rowIndex]
