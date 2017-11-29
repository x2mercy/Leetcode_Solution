class Solution(object):
    def multiply(self,num1, num2):
        if num1=="0" and num2=="0":
            return "0"
        if len(num1)<len(num2):
            num1,num2=num2,num1
        i=len(num2)-1
        res1=0
        result=0
        while i>=0:
            digit=self.digitmul(num2[i],num1,res1)
            res1=digit*(10**(len(num2)-i-1))
            result+=res1
            i-=1
        result=str(result)
        return result

    def digitmul(self,num2,num1,res1):
        cin=0
        res2=0
        digit=0
        j=len(num1)-1
        while j>=0:
            res2=int(num2)*int(num1[j])+cin
            if res2>9:
                if j!=0:
                    cin=res2//10
                    res2=res2%10
            else:
                cin=0
            digit+=res2*(10**(len(num1)-j-1))
            j-=1
        return digit
        
