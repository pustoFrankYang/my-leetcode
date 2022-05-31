# class Solution:
#     def hasAllCodes(self, s: str, k: int) -> bool:
#         checker = 0
#         for i in range(len(s) - k + 1):
#             checker |= 1 << int(s[i:i + k], 2)
#         return checker == 2 ** (2 ** k) - 1
    
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 2 ** k
        got = [False] * need
        for i in range(len(s) - k + 1):
            val = int(s[i:i + k], 2)
            if not got[val]:
                need -= 1
                got[val] = True
                if need == 0:
                    return True
        return False