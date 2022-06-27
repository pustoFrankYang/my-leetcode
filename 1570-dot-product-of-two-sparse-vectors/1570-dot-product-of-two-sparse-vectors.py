class SparseVector:
    def __init__(self, nums: List[int]):
        self.m = {}
        for i in range(len(nums)):
            if nums[i]:
                self.m[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for k, v in self.m.items():
            ans += v * vec.m.get(k, 0)
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)