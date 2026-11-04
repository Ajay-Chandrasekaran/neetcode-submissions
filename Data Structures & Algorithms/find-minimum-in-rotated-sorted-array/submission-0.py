class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while nums[l] > nums[r]:
            m = (l + r ) // 2
            l = m
        return nums[l] 