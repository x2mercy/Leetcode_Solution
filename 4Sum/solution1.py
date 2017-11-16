#timeout
#陆续改了一天的代码！居然超时了！欺负python慢么！
import copy
class Solution(object):

    def fourSum(self,nums, target):
        result=[]
        nums.sort()
        a=[]
        for i in range(len(nums)):
            nums_copy=copy.deepcopy(nums)
            nums_copy.remove(nums[i])
            sum_nums=self.threesum(nums_copy,target-nums[i],nums[i])
            for j in sum_nums:
                if j in result:
                    sum_nums.remove(j)
            result+=(sum_nums)
        for i in result:
            if i not in a:
                a.append(i)
        return a
    def threesum(self,nums,target,nums2):
        sum_nums=[]
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                add=[]
                s=nums[i]+nums[l]+nums[r]
                if s==target:
                    add.append(nums[i])
                    add.append(nums[l])
                    add.append(nums[r])
                    add.append(nums2)
                    add.sort()
                    if add not in sum_nums:
                        sum_nums.append(add)
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif s<target:
                    l+=1
                elif s>target:
                    r-=1

        return sum_nums
        
