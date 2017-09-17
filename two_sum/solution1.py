#方法：enumerate+try...except...
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,val in enumerate(nums):
            try:
                j=nums.index(target-val)
                if j!=i:
                    return i,j
                else:
                    continue
            except ValueError:
                continue
        
