class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        checker = 0
        for i in range(len(s) - k + 1):
            # print(s[i:i + k])
            checker |= 1 << int(s[i:i + k], 2)
        # print(bin(checker))
        return checker == 2 ** (2 ** k) - 1