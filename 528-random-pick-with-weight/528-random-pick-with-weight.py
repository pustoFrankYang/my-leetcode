class Solution:
# calc a list of accu sums
# when pick, pick from [0, sum] and binary search it, left end
# e.g. [1,1] => [1,2]
    def __init__(self, w: List[int]):
        self.sum = w.copy()
        for i in range(1, len(self.sum)):
            self.sum[i] += self.sum[i - 1]
            
    def pickIndex(self) -> int:
        target = random.random() * self.sum[-1]
        l, r = 0, len(self.sum)
        while l < r:
            m = (r - l) // 2 + l
            if self.sum[m] >= target:
                r = m
            else:
                l = m + 1
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()