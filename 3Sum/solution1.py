import copy
class Solution(object):
    def threeSum(self,nums):
        result=[]
        i=0
        zero=[]
        if nums.count(0)>=3:
            zero=[0,0,0]
            result.append(zero)
        for i in range(len(nums)):   
            zero=[]
            for j in range(i+1,len(nums)):
                nums_copy=copy.deepcopy(nums)
                if -(nums[i]+nums[j]) in nums:
                    one=nums[i]
                    nums_copy.remove(one)
                    two=nums[j]
                    nums_copy.remove(two)
                    if not -(one+two) in nums_copy:
                        break
                    three=-(nums[i]+nums[j])
                    zero.append(one)
                    zero.append(two)
                    zero.append(three)
                    tag=0
                    for n in range(len(result)):
                        flag=0
                        for m in range(len(zero)):
                            if zero[m] in result[n]:
                                flag+=1
                        if flag==3:
                            break
                        else:
                            tag+=1
                            continue
                    if tag==len(result):
                        result.append(zero)
                    zero=[]
                    
        return result
