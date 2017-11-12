# time limit exceed!
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area=0
        current_area=0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                current_area=(j-i)*min(height[i],height[j])
                if current_area>max_area:
                    max_area=current_area
        return max_area
            
