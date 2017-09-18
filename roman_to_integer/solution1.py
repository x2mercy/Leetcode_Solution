class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_nums={'I':1,
                    'V':5,
                   'X':10,
                    'L':50,
                    'C':100,
                    'D':500,
                    'M':1000}
        roman=('I','V','X','L','C','D','M')
        current_num=0
        for i in range(len(s)):
            if i<len(s)-1:
                current_roman=s[i].upper()
                next_roman=s[i+1].upper()
                new_num=roman_nums[current_roman]
                if roman_nums[current_roman]<roman_nums[next_roman]:
                    current_num-=new_num
                if roman_nums[current_roman]>=roman_nums[next_roman]:
                    current_num+=new_num
            if i==len(s)-1:
                current_roman=s[i].upper()
                new_num=roman_nums[current_roman]
                current_num+=new_num
        return current_num
