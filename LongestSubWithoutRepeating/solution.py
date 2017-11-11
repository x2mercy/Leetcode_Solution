class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        if len(s)==1:
            return 1
        start=0
        max_s=0
        nums={}
        for i in range(len(s)):
            if s[i] in nums and start<=nums[s[i]]:  
                start=nums[s[i]]+1
            else:
                nums[s[i]]=i
                max_s=max(max_s,i-start+1)
            nums[s[i]]=i
        
        return max_s
