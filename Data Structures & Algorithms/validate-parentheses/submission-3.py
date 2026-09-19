class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif c == ']' and (len(stack) < 1 or stack[-1] != '['):
                return False
            elif c == ')' and (len(stack) < 1 or stack[-1] != '('):
                return False
            elif c == '}' and (len(stack) < 1 or stack[-1] != '{'):
                return False
            else:
                stack.pop(-1)
        return len(stack) == 0