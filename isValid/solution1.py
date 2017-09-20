class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        dic={")":"(","]":"[","}":"{"}
        for i in s:
             if len(s)%2!=0:
                    return False
             if i=="(" or i=="[" or i=="{":
                stack.append(i)
             else:
                if not stack or stack[-1]!=dic[i]:
                    return False
                else:
                    stack.pop()
        return not stack
