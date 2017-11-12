class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        result=['']*numRows
        index=0 
        j=1
        for i in range(0,len(s)):
            result[index]+=s[i]
            if index==0:
                j=1
            elif index==numRows-1:
                j=-1
            index+=j
        
        
        return ''.join(result)
        
