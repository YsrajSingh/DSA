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
            is_exists = brackets.get(i)
            if is_exists:
                if stack and stack[-1] == is_exists:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return len(stack) == 0


        