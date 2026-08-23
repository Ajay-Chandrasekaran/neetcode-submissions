class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq: dict[int, int] = dict()

        for e in s:
            freq[e] = freq.get(e, 0) + 1
        for e in t:
            freq[e] = freq.get(e, 0) - 1
        
        return all(v == 0 for v in freq.values())