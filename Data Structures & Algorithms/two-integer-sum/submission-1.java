class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i=0; i<nums.length; i++) {
            map.put(nums[i], i);
        }
        
        int rem = -1;

        for (int j=0; j<nums.length; j++) {
            rem = map.getOrDefault(target - nums[j], -1);

            if (rem != j && rem != -1) {
                return new int[]{j, rem};
            }
        }
        return new int[]{-1, -1};
    }
}
