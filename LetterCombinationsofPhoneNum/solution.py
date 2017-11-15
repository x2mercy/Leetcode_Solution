from itertools import product
class Solution(object):
    def letterCombinations(self,digits):
        alpha=[]

        if digits=="":
            return []
        result=[]
        nums={'1':'',
            '2':'abc',
          '3':'def',
          '4':'ghi',
          '5':'jkl',
          '6':'mno',
          '7':'pqrs',
          '8':'tuv',
          '9':'wxyz',
          '0':''}
        alpha=[c for c in nums[digits[0]]]
        for i in digits[1:]:
            alpha=product(alpha,nums[i])
            alpha=[''.join(item) for item in alpha]
        result=alpha
        return result   
        
        
        
            
                
        
            
        
