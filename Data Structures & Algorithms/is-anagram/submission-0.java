class Solution {
    public boolean isAnagram(String s, String t) {
        int[] word1 = new int[26];
        int[] word2 = new int[26];

        for (char c: s.toCharArray()) {
            ++word1[c - 'a'];
        }

        for (char d: t.toCharArray()) {
            ++word2[d - 'a'];
        }

        for (int i=0; i<26; i++) {
            if (word1[i] != word2[i])
                return false;
        }

        return true;
    }
}
