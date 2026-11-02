class Solution {
    public int[] canSeePersonsCount(int[] heights) {
        int len = heights.length;
        int[] res = new int[len];

        if (len == 1) {
            return res;
        }

        Stack<Integer> stack = new Stack<>();
        stack.push(heights[len - 1]);

        for (int i=len-2; i>=0; i--) {
            int visible = 0;

            while (!stack.empty() && heights[i] > stack.peek()) {
                ++visible;
                stack.pop();
            }

            res[i] = (stack.empty()) ? visible : visible + 1;
            stack.push(heights[i]);
        }

        return res;
    }
}