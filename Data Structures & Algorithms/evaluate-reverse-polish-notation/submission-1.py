class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        eval_stack = []

        for c in tokens:
            if c not in ['+', '-', '*', '/']:
                eval_stack.append(c)
            else:
                r = eval_stack.pop()
                l = eval_stack.pop()

                res = int(eval(l + c + r))
                eval_stack.append(str(res))
        return int(eval_stack[0])