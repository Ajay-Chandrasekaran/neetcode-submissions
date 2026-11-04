class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() < 2) return s.length();

        int maxLen = 0;
        int l = 0, r = 1;
        Set<Character> seen = new HashSet<>();
        seen.add(s.charAt(l));

        while (r < s.length()) {
            while(seen.contains(s.charAt(r))) {
                seen.remove(s.charAt(l));
                l++;
            }
            seen.add(s.charAt(r));
            maxLen = Math.max(maxLen, seen.size());
            r++;
        }

        return maxLen;
    }
}
