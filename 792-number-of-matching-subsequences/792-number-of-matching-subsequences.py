# Q792m, runtime 27.60%
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        c2p = [[] for _ in range(26)]  # char to positions
        for i, ch in enumerate(s):
            c2p[ord(ch) - ord('a')].append(i)
        ans = 0
        for word in words:
            curr = -1
            cans = 1
            for c in word:
                bis = bisect.bisect(c2p[ord(c) - ord('a')], curr)
                if bis >= len(c2p[ord(c) - ord('a')]):
                    cans -= 1
                    break
                curr = c2p[ord(c) - ord('a')][bis]
            ans += cans
        return ans