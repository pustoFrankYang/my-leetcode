class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortednums = sorted(nums)
        p, q = 0, len(nums) - 1
        while p < len(nums) and nums[p] == sortednums[p]:
            p += 1
        while q >= 0 and nums[q] == sortednums[q]:
            q -= 1
        if p >= q:
            return 0
        else:
            return q - p + 1