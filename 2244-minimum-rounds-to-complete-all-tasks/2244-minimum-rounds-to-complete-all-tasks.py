class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        m = {}
        for t in tasks:
            m[t] = m.get(t, 0) + 1
        ans = 0
        for k, v in m.items():
            if v == 1:
                return -1
            if v % 2:
                ans += 1
                v -= 3
            ans += v // 3
            if v % 3:
                ans += 1
        return ans