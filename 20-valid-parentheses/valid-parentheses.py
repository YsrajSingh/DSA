class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        brackets = {
            "}": "{",
            "]": "[",
            ")": "(",
        }
        
        stack = []
        
        for i in s:
            if i in brackets:
                if stack and stack[-1] == brackets[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return len(stack) == 0


        