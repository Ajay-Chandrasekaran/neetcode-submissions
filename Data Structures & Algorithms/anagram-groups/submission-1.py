class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            key = self.get_key(s)
            if not key in groups:
                groups[key] = []
            groups.get(key).append(s)
        
        return list(groups.values())

    def get_key(self, s: str):
        key = [0] * 26

        for ch in s:
            key[ord(ch) - ord('a')] += 1
        
        return ','.join(map(str, key))
