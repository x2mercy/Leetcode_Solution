class Solution(object):
    def combinationSum(self,candidates, target):
        result=[]
        candidates.sort()
        self.check(candidates,0,[],target,result)
        return result
    
    def check(self,num,index,path,target,result):
        if target<0:
            return
        elif target==0:
            result.append(path)
            return
        else:
            for i in range(index,len(num)):
                self.check(num,i,path+[num[i]],target-num[i],result)
    
        
