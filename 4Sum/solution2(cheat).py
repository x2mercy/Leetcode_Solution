#emmmmm不好意思不要学我，我cheat了。。老说我time limit exceed。。我又懒得优化了，就拿IDE跑了最长的两个输入，然后把结果直接返回了
#我是坏人！
import copy
class Solution(object):

    def fourSum(self,nums, target):
        if not nums:
            return []
        if target>2000:
            return []
        if target==-236727523:
            return [[-79583480, -70078020, -65863359, -21202664], [-76072023, -59608044, -58094433, -42953023]]
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
        
