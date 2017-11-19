class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums==[]:
            return [-1,-1]
        result=[]
        final=[]
        try:
            first=nums.index(target)
        except:
            return [-1,-1]
        result.append(first)
        for i in range(first+1,len(nums)):
            if nums[i]==target:                    
                result.append(i) 
        result.sort()
        if len(result)==1:
            result.append(result[0])
        final.append(result[0])
        final.append(result[len(result)-1])
        return final
