class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums==[]:
            return -1
        if len(nums)==1:
            if target==nums[0]:
                return 0
            else:
                return -1
        min_num=min(nums)
        index=nums.index(min_num)
        right=nums[len(nums)-1]
        left=nums[0]
        if sorted(nums)==nums or sorted(nums,reverse=True)==nums:
            for i in range(len(nums)):
                if target==nums[i]:
                    return i
            return -1
        if left==target:
            return 0
        if right==target:
            return len(nums)-1
        if target==min_num:
            return index
        if target>left:#left part
            for i in range(0,index):
                if target==nums[i]:
                    return i
            return -1
        elif target<right and target>min_num:#right part
            for i in range(index+1,len(nums)):
                if target==nums[i]:
                    return i
            return -1
        else:
            return -1
