class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Initialize the farthest index you can reach
        farthest = 0

        # Traverse the list
        for i in range(len(nums)):
            # If we are at an index that we cannot reach, return False
            if i > farthest:
                return False
            
            # Update the farthest index we can reach from the current index
            farthest = max(farthest, i + nums[i])
            
            # If we can reach or go beyond the last index, return True
            if farthest >= len(nums) - 1:
                return True
        
        # If we finish the loop and can't reach the last index, return False
        return False

            