from collections import defaultdict

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chars = defaultdict(str)
        chars[")"] = "("
        chars["]"] = "["
        chars["}"] = "{"

        for c in s:
            stack.append(c)
            if len(stack) >= 2 and stack[-2] == chars[stack[-1]]:
                stack.pop(-2)
                stack.pop(-1)
        
        if not stack:
            return True
        else: 
            return False