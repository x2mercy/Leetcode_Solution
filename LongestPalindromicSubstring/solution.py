
#Time Limit Exceed
class Solution(object):
    def longestPalindrome(self,s):
        if s=="":
            return ""
        result={}
        if len(s)==1:
            return  s
        tag=0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                l=i
                r=j
                sub=s[i:j+1]
                flag=0
                while l<r:
                    if s[l]==s[r]:
                        l+=1
                        r-=1
                    else:
                        flag+=1
                        break
                if flag!=1:
                    result[sub]=j-i+1
                    tag+=1
                else:
                    continue
        if tag!=0:
            return max(result,key=result.get)
        else:
            return s[0]
        
        
                    
            
                    
        
        
