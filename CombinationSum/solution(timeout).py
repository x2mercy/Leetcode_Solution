#time limit exceed
class Solution(object):
    def combinationSum(self,candidates, target):
        result=[]
        candidates.sort()
        self.check(candidates,[],target,result)
        return result
    
    def check(self,num,path,target,result):
        if target<0:
            return
        elif target==0:
            path.sort()
            if path not in result:
                result.append(path)
            return
        else:
            for i in range(0,len(num)):
                self.check(num,path+[num[i]],target-num[i],result)
    
        
