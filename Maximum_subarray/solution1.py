class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        else:
            current=nums[0]
            max_sums=nums[0]
            for i in range(1,len(nums)):
                current=max(nums[i],current+nums[i])
                max_sums=max(current,max_sums)
            return max_sums   
        
