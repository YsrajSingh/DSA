class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        
        farthest = 0
        jumps = 0
        current_end = 0

        for i in range(len(nums)):
            # Update the farthest we can reach
            farthest = max(farthest, i + nums[i])
            
            # If we reach the end of the current jump range
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # If we can already reach the last index, break early
                if current_end >= len(nums) - 1:
                    break
        
        return jumps
                