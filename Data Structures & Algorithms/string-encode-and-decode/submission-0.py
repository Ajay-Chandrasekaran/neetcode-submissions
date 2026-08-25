class Solution:

    def encode(self, strs: List[str]) -> str:
        result = [str(len(s)) + '#' + s for s in strs]
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0
        str_len = 0
        while i < len(s):
            if s[i] != '#':
                str_len = str_len * 10 + int(s[i])
                i += 1
            else:
                i += 1
                result.append(s[i:i+str_len])
                i = i + str_len
                str_len = 0
        return result