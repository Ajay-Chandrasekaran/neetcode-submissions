class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif c == '(' and len(stack) > 0 and stack[-1] == ')':
                stack.pop(-1)
            elif c == '[' and len(stack) > 0 and stack[-1] == ']':
                stack.pop(-1)
            elif c == '{' and len(stack) > 0 and stack[-1] == '}':
                stack.pop(-1)
            else:
                return True
        return False