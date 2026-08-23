class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = dict()

        for i, e in enumerate(nums):
            if e in seen:
                return True

            seen[e] = i
        
        return False
