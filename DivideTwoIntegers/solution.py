class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag=0
        sign1=1
        sign2=1
        result=0
        if dividend<0:
            sign1=0
        if divisor<0:
            sign2=0
        dividend=abs(dividend)
        divisor=abs(divisor)
        if dividend==0:
            return 0
        if dividend<divisor:
            return 0
        while dividend>=divisor:
            temp=divisor
            i=1
            while dividend>=temp:
                dividend-=temp
                result+=i
                i<<=1#i=i*2
                temp<<=1#temp=tempt*2
        sign=sign1 ^ sign2
        if sign==1:
            result= -result
        return min(max(-2147483648, result), 2147483647)
        
