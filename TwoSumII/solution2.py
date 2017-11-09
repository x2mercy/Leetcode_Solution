class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #dictionary algorithm
        result={}
        for i in range(len(numbers)):
            if target-numbers[i] in result:
                return [result[target-numbers[i]]+1,i+1]
            else:
                result[numbers[i]]=i
                
        
