class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas)==1:
            if gas[0]>=cost[0]:
                return 0
            else:
                return -1
        diff=[]
        for i in range(len(gas)):
            diff.append(gas[i]-cost[i])
        sum_gas=0
        index=0
        before=0
        for i in range(len(diff)):
            if sum_gas<before:
                before=sum_gas
                index=i
            sum_gas=sum_gas+diff[i]
        if sum_gas<0:
            return -1
        return index
            
        
