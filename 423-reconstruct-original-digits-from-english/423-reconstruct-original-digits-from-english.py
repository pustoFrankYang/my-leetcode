class Solution:
    def originalDigits(self, s: str) -> str:
        cnt = defaultdict(int)
        dcnt = [0] * 10
        ans = ''
        for ch in s:
            cnt[ch] += 1
        for i, word in [
            (0, 'zero'), (6, 'six'), (8, 'eight'), (2, 'two'), (4, 'four'),
            (7, 'seven'), (5, 'five'), (9, 'nine'), 
            (3, 'three'), (1, 'one')
        ]:
            mincnt = float('inf')
            for ch in word:
                currcnt = cnt[ch]
                if ch == 'e' and (word == 'three' or word == 'seven'):
                    currcnt //= 2
                if ch == 'n' and (word == 'nine'):
                    currcnt //= 2
                if cnt[ch] < mincnt:
                    mincnt = cnt[ch]
            if mincnt < float('inf'):
                dcnt[i] += mincnt
                for ch in word:
                    cnt[ch] -= mincnt
        for i, n in enumerate(dcnt):
            ans += str(i) * n
        return ans