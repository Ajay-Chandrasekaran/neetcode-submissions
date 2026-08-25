class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_product = [0] * len(nums)
        l_product[0] = nums[0]
        for i in range(1, len(nums)):
            l_product[i] = l_product[i-1] * nums[i]
        
        r_product = [0] * len(nums)
        r_product[-1] = nums[-1]
        for j in range(len(nums)-2, 0, -1):
            r_product[j] = r_product[j+1] * nums[j]
        
        result = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                result[i] = r_product[i+1] 
            elif i == len(nums) - 1:
                result[i] = l_product[i-1]
            else:
                result[i] = l_product[i-1] * r_product[i+1]
        
        return result