class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        int rem = -1;

        for (int i=0; i<nums.length; i++) {
            rem = map.getOrDefault(target - nums[i], -1);
            
            if (rem != -1) {
                return new int[]{rem, i};
            }
            map.put(nums[i], i);
        }

        return new int[]{-1, -1};
    }
}
