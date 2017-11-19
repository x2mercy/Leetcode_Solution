class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if sorted(nums, reverse=True) == nums:
            nums.sort()
        else:
            last_index=0
            for i in range(len(nums)-1):
                if nums[i]<nums[i+1]:
                    last_index=max(i,last_index)
            index_bigger=0
            for i in range(len(nums)):
                if nums[last_index]<nums[i]:
                    index_bigger=max(index_bigger,i)
            nums[index_bigger],nums[last_index]=nums[last_index],nums[index_bigger]
            nums[last_index+1:] = sorted(nums[last_index+1:])
            
