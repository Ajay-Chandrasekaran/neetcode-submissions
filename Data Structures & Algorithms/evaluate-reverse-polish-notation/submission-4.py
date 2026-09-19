class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c not in ['+', '-', '*', '/']:
                stack.append(int(c))
            else:
                r = stack.pop()
                l = stack.pop()
                match c:
                    case '+':
                        stack.append(l + r)
                    case '-':
                        stack.append(l - r)
                    case '*':
                        stack.append(l * r)
                    case '/':
                        stack.append(int(l / r))
        return stack[0]