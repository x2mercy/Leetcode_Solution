#dp
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()                      
        result = []
        self.check(candidates, 0, [], result, target)
        return result
    
    def check(self, nums, start, path, result, target):
        if not target:
            result.append(path)
            return
    
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target:
                break
            self.check(nums, i + 1, path + [nums[i]], 
                           result, target - nums[i])
