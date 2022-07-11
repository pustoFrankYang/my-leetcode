# ¡¡¡gesah
# Q2333m, 
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        
        h = [-abs(x - y) for x, y in zip(nums1, nums2)]
        if -sum(h) < k1 + k2:
            return 0
        chance = k1 + k2
        heapq.heapify(h)
        n = len(nums1)
        while chance > 0:
            curr = -heapq.heappop(h)
            reducer = max(chance // n, 1)
            curr -= reducer
            chance -= reducer
            heapq.heappush(h, -curr)
        return sum(pow(x, 2) for x in h)
                