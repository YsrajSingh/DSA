class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniqueNumber = 0
        for num in nums:
            uniqueNumber ^= num
        
        return uniqueNumber
        