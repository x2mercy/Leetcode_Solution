class Solution(object):
    def threeSum(self,nums):
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            zero=[]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                zero=[]
                s=nums[i]+nums[l]+nums[r]
                if s<0:
                    l+=1
                elif s>0:
                    r-=1
                else:
                    zero.append(nums[i])
                    zero.append(nums[l])
                    zero.append(nums[r])
                    result.append(zero)
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return result
