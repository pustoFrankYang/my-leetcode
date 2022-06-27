class SparseVector:
    def __init__(self, nums: List[int]):
        self.m = []
        for i in range(len(nums)):
            if nums[i]:
                self.m.append((i, nums[i]))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        p = q = ans = 0
        while p < len(self.m) and q < len(vec.m):
            if self.m[p][0] == vec.m[q][0]:
                ans += self.m[p][1] * vec.m[q][1]
                p += 1
                q += 1
            elif self.m[p][0] < vec.m[q][0]:
                p += 1
            else:
                q += 1
        # if p 
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)