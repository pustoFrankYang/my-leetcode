# ¡¡¡gesah
class Solution:
    def reorganizeString(self, s: str) -> str:
        cnts = [0] * 26
        maxc = 0
        maxid = 0
        for ch in s:
            cnts[ord(ch) - ord('a')] += 1
            if cnts[ord(ch) - ord('a')] > maxc:
                maxc = cnts[ord(ch) - ord('a')]
                maxid = ord(ch) - ord('a')
        if maxc > (len(s) + 1) // 2:
            return ""
        ans = " " * len(s)
        isOdd = 0
        p = 0
        for i in range(cnts[maxid]):
            ans = ans[:2 * p + isOdd] + chr(ord('a') + maxid) + ans[2 * p + isOdd + 1:]
            p += 1
        cnts[maxid] = 0
        for ind in range(26):
            for i in range(cnts[ind]):
                if isOdd == 0 and p * 2 >= len(s):
                    isOdd = 1
                    p = 0
                ans = ans[:2 * p + isOdd] + chr(ord('a') + ind) + ans[2 * p + isOdd + 1:]
                p += 1
        return ans