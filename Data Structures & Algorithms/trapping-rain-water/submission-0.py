class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        l = 0
        r = 1
        total_water = 0
        water = 0

        while r < len(height):
            if height[r] >= height[l]:
                total_water += water
                l = r
                water = 0
            else:
                water += height[l] - height[r]
            r += 1
        
        return total_water