class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p1 = p2 = 0
        l_p1, l_p2 = len(s), len(t)
        
        while p2 < l_p2:
            if p1 == l_p1:
                return True
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1
        
        return p1 == l_p1
