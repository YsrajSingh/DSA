class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        i, j = len(s) - 1, len(s) - 1
        result = []
        
        while i >= 0:
            while i >= 0 and s[i] != " ":
                i -= 1
            result.append(s[i + 1 : j + 1])
            
            while i >= 0 and s[i] == " ":
                i -= 1
            j = i

        return " ".join(result)