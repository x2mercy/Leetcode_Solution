class Solution:
    # @param n, an integer
    # @return an integer
    
    def reverseBits(self, n):
        result=0
        for i in range(0,32):
            result+=n & 1
            n=n>>1
            if i<31:
                result=result<<1
        return result
            
