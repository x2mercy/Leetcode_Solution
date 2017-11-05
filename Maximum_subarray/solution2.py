# This solution is not perfect because  Time Limit Exceeded will happen when input a list with a lot of numbers
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        else:
            max_s=[]
            for i in range(len(nums)):
                current_sums=nums[i]
                for j in range(i+1,len(nums)):
                    current_sums+=nums[j]
                    max_s.append(current_sums)
            for i in range(len(nums)):
                max_s.append(nums[i])
            max_s.sort()
            return max_s[len(max_s)-1]
