class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_jump=0
        for i in range(len(nums)):
            if i>max_jump:
                return False
            else:
                max_jump=max(max_jump,nums[i]+i)
                if max_jump==len(nums)-1:
                    break
        return True
        
