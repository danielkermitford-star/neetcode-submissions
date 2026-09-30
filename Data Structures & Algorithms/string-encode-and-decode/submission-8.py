class Solution:

    def encode(self, strs: List[str]) -> str:
        strs2 = []
        for s in strs:
            strs2.append(str(len(s)) + '&' + s)
        return "".join(strs2)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i+1;
            while j < len(s):
                if s[j] == '&':
                    str_len = int(s[i:j])
                    break;
                j += 1
            j += 1
            i = j + str_len
            strs.append(s[j:i])
        return strs
            