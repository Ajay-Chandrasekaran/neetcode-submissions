class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, e in enumerate(temperatures):
            while len(stack) > 0 and temperatures[stack[-1]] < e:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)
        return result