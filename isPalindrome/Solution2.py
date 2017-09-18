#reference: RealHacker/leetcode-solutions/009_palindrome_number/palindrome_number.py
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if x==0:
            return True
        l=len(str(x))
        i=1
        x1=x2=x
        while i<=l/2:
            left=x1/10**(l-i)
            x1%=10**(l-i)
            right=x2%10
            x2/=10
            if right!=left:
                return False
            else:
                i+=1
        return True
