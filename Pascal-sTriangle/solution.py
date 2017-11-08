class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        result=[]
        result.append([1])
        if numRows==1:
            return result
        result.append([1,1])
        if numRows==2:
            return result
        
        for i in range(2,numRows):
            nums=[]
            nums.append(1)
            while len(nums)<i:
                nums.append(result[i-1][len(nums)-1]+result[i-1][len(nums)])
            nums.append(1)
            result.append(nums)
        return result
                
        
