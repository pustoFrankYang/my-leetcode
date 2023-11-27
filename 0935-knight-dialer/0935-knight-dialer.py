class Solution:
    def knightDialer(self, n: int) -> int:
        next = [[0] * 10 for _ in range(10)]
        next[0][4] = next[0][6] = next[1][6] = next[1][8] = next[2][7] = next[2][9] = 1
        next[3][4] = next[3][8] = next[4][0] = next[4][3] = next[4][9] = next[6][0] = 1
        next[6][1] = next[6][7] = next[7][2] = next[7][6] = next[8][1] = next[8][3] = 1
        next[9][2] = next[9][4] = 1
        ans = 0
        curr = [1] * 10
        for _ in range(n - 1):
            new = [0] * 10
            for n in range(10):
                # 还真不知道这一步就可以做mod运算了
                new[n] = sum([curr[x] * next[n][x] for x in range(10)]) % (1000000007)
            curr = new
        return sum(curr)  % (1000000007)