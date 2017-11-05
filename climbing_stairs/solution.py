class Solution(object):
    def climbStairs(self,n):
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        ways=[]
        for i in range(0,n+1):
            if i==0:
                ways.append(0)
            elif i==1:
                ways.append(1)
            elif i==2:
                ways.append(2)
            else:
                ways.append(ways[i-1]+ways[i-2])
        return ways[len(ways)-1]
