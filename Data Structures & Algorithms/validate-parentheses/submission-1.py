class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if stack and ((stack[-1] == '{' and b == '}') or (stack[-1] == '[' and b == ']') or (stack[-1] == '(' and b == ')')):
                stack.pop()
            else:
                stack.append(b)
        if len(stack) == 0:
            return True
        return False