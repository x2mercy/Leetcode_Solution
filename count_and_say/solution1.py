class Solution(object):
    def countAndSay(self, n):
        s="1"
        for i in range(n-1):
            nums=""
            index=0
            for j in range(1,len(s)):
                if s[j]!=s[j-1]:
                    nums+=str(j-index)+s[index]
                    index=j
            nums+=str(len(s)-index)+s[index]
            s=nums
        return s
