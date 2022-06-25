class Solution:
    def distinctSequences(self, n: int) -> int:
        # [n] [a] [b] w.r.t. current point c
        # dp = [[[0 for i in range(7)] for _ in range(7)] for _ in range(10001)]
        
        @functools.lru_cache(None)
        def dfs(n, a, b):
            ans = 0
            if n == 0:
                return 1
            # avoid repeated
            # if dp[n][a][b] != 0:
            #     return dp[n][a][b]
            # c is current point, after a, b
            for c in range(1, 7):
                # a == b == 0 at beginning
                if b == 0 or (c != a and c != b and math.gcd(c, b) == 1):
                    # dp[n][a][b] = (dp[n][a][b] + dfs(n - 1, b, c)) % (10**9 + 7)
                    ans += dfs(n - 1, b, c)
            return ans % (10**9 + 7)
            
        return dfs(n, 0, 0)