class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        map = {}
        stack = []
        for i, e in enumerate(position):
            map[e] = i
        
        position.sort()

        for i in range(len(position)-1, -1, -1):
            time = (target - position[i]) / speed[map[position[i]]]

            if len(stack) == 0 or stack[-1] < time:
                stack.append(time)
        
        return len(stack)