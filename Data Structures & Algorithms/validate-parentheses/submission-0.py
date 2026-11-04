class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == '{' or ch == '(' or ch == '[':
                stack.append(ch)
            elif (ch == '}' and stack[-1] != '{') or (ch == ')' and stack[-1] != '(') or (ch == ']' and stack[-1] != '['):
                return False
            else:
                stack.pop(-1)
        
        return True
                