#Also Time Limit Exceed!!!!!
class Solution(object):
    def longestPalindrome(self,s):
        if s=="":
            return ""
        if len(s)==1:
            return s
        tag=0
        max_length=0
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
                    if max_length<j-i+1:
                        max_length=j-i+1
                        longest=s[i:max_length+i]
                        tag+=1
                    else:
                        continue
        if tag!=0:
            return longest
        else:
            return s[0]
        
        
                    
            
                    
        
        
