class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        list = sorted(citations, reverse=True)
        count = 0
        for i in range(0, len(list)):
            if list[i] > i:
                count +=1

        return count