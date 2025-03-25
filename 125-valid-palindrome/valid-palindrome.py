class Solution(object):
    def strip_non_alphanumeric(self, s):
        return re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = self.strip_non_alphanumeric(s)
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True