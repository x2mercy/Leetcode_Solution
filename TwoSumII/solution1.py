class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
#        result=[]
#        if numbers==None:
#            return []
#        for i in range(0,len(numbers)-1):
#            for j in range(1,len(numbers)):
#                if i==j:
#                    continue
#                if numbers[i]+numbers[j]==target:
#                    result.append(i+1)
#                    result.append(j+1)
#                    return result
        l=0
        r=len(numbers)-1
        while l<r:
            sum_num=numbers[l]+numbers[r]
            if sum_num==target:
                return [l+1,r+1]
            elif sum_num<target:
                l+=1
            elif sum_num>target:
                r-=1
        
