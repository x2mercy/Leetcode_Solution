class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s==target:
                    return s
                if abs(target-s)<abs(target-result):
                    result=s
                if s<target:
                    l+=1
                elif s>target:
                    r-=1
        return result
            
            
            
            
