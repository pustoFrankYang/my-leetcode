class Solution:
    def countOrders(self, n: int) -> int:
        ans = 1
        for i in reversed(range(1, 2 * n + 1)):
            if i % 2 == 0:
                ans = (ans * (i // 2)) % (10 ** 9 + 7)
            else:
                ans = (ans * i) % (10 ** 9 + 7)
                
        return ans