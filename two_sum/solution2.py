#refer:https://github.com/x2mercy/LeetCode/blob/master/001%20Two%20Sum.py#L29
#方法：hashmap
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map={}
        for i,val in enumerate(nums):
            hash_map[val]=i
        for j,val in enumerate(nums):
            if target-val in nums:
                k=hash_map[target-val]
                if j!=k:
                    return j,k
