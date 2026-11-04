class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for i, e in enumerate(nums):
            seen[e] = i
        
        for i, e in enumerate(nums):
            if (target - e) in seen:
                return [i, seen[target - e]]
