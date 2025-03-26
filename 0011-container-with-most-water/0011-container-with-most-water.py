class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0 
        
        while left < right:
            overflow = min(height[left], height[right])
            width = right - left
            max_area = max(max_area, overflow * width)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area