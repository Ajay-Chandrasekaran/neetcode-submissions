class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();

        for (String s: strs) {
            var key = freqArr(s);
            List<String> group = map.get(key);

            if (group == null) {
                group = new ArrayList<String>();
                map.put(key, group);
            }

            group.add(s);
        }

        return new ArrayList<>(map.values());
    }

    private String freqArr(String s) {
        int[] key = new int[26];

        for (char c: s.toCharArray()) {
            ++key[c - 'a'];
        }

        return Arrays.toString(key);
    }
}
