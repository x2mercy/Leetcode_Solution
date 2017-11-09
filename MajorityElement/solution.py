class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result={}
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            if nums[i] in result:
                result[nums[i]]=result[nums[i]]+1
                if result[nums[i]]>len(nums)/2:
                    return nums[i]
            else:
                result[nums[i]]=1
                
        
