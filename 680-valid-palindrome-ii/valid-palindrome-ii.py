class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        
        def isPalindrome(sub, left, right):
            while left < right:
                if sub[left] != sub[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(s, left+1, right) or isPalindrome(s, left, right-1)
            left += 1
            right -= 1
        
        return True