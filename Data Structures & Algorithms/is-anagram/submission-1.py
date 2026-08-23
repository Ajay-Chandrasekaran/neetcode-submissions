class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_freq = dict()
        
        for e in s:
            if e in s_freq:
                s_freq[e] += 1
            else:
                s_freq[e] = 1
        
        t_freq = dict()

        for e in t:
            if e in t_freq:
                t_freq[e] += 1
            else:
                t_freq[e] = 1
        
        try:
            for k in s_freq:
                if s_freq[k] != t_freq[k]:
                    return False
        except:
            return False
        
        return True