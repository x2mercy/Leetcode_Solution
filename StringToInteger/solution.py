class Solution(object):
    def myAtoi(self,str):
        result=0
        sign=1
        i=0
        INT_MAX=2147483647
        INT_MIN=-2147483648
        flag=0
        start=0
        if str=="":
            return 0
        for i in range(len(str)):
            start=i
            if str[i]=='+':
                flag+=1
                sign=1
                start+=1
                break
            if str[i]=='-':
                flag+=1
                sign=-1
                start+=1
                break
            if not str[i].isdigit() and str[i]!=' ':
                return 0
            if str[i].isdigit():
                break
        for i in range(start,len(str)):
            if not str[i].isdigit() and result==0 and str[i]!=' ':
                break
            elif str[i]==' ' and flag==0:
                continue
            elif str[i]==' ' and flag!=0:
                break                
            elif not str[i].isdigit() and flag!=0:
                break
            else:
                flag+=1
                result=result*10+int(str[i])
            if sign==1 and result>INT_MAX:
                return INT_MAX
            if sign==-1 and result*sign<INT_MIN:
                return INT_MIN
        return int(result)*sign
