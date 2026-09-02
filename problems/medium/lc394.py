class Solution:
    def extendString(self, s: str, i: int) -> (int, str):
        res = ""
        while i < len(s):
            if s[i].isdigit():
                k = 0
                while i < len(s) and s[i].isdigit():
                    k = k * 10 + int(s[i])
                    i += 1
                i += 1
                next_i, next_str = self.extendString(s, i)
                res += next_str * k
                i = next_i + 1
            elif s[i] == "]":
                return i, res
            else:
                res += s[i]
                i += 1
        return len(s) - 1, res

    def decodeString(self, s: str) -> str:
        _, res = self.extendString(s, 0)
        return res
