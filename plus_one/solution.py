class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits)==1 and digits[0]==0:
            digits[0]=1
            return digits
        digits.reverse()
        cin=1
        for i in range(len(digits)):
            add=digits[i]+cin
            if add==10:
                cin=1
                digits[i]=0
                if i==len(digits)-1:
                    digits.append(cin)
            else:
                cin=0
                digits[i]=add
        digits.reverse()
        return digits
