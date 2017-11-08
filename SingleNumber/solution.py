class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result={}
        for i in range(len(nums)):
            result[nums[i]]=result.get(nums[i],0)+1
        keys=result.keys()
        for i in keys:
           if result[i]==1:
                return i
            
            
            
            
