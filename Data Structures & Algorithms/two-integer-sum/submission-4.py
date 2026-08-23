class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for i, e in enumerate(nums):
            seen[e] = i
        
        for i, e in enumerate(nums):
            if (target - e) in seen and i != seen[target - e]:
                return [i, seen[target - e]]
