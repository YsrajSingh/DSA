class Solution(object):
    def strip_non_alphanumeric(self, s):
        return re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return s == s[::-1]  # Efficient palindrome check using slicing
