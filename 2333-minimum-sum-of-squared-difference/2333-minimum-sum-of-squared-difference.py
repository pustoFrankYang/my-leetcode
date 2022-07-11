# ¡¡¡gesah
# Q2333m, 9.18%
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        chance = k1 + k2
        h = [-abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
        if -sum(h) < chance:
            return 0
        heapq.heapify(h)
        n = len(nums1)
        while chance > 0:
            curr = -heapq.heappop(h)
            reducer = max(chance // n, 1)
            curr -= reducer
            chance -= reducer
            heapq.heappush(h, -curr)
        return sum(x**2 for x in h)
                