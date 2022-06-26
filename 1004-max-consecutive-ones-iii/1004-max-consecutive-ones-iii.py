class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = cnt0 = 0
        # r not included
        maxlen = r - l
        # init
        while r < len(nums) and (nums[r] == 1 or cnt0 < k):
            if nums[r] == 0:
                cnt0 += 1
            r += 1
        maxlen = r - l
        while r + 1 < len(nums):
            # move r to next; r must be at a 0, so consume the new 0
            r += 1
            while r < len(nums) and nums[r] == 1:
                r += 1
            # move l to next; l will be set to the pos next to next 0
            while l < r and nums[l] == 1:
                l += 1
            l += 1
            maxlen = max(maxlen, r - l)
        return maxlen
                