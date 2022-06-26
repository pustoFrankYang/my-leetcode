class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = cnt0 = 0
        # r not included
        currlen = r - l
        # init
        while r < len(nums) and (nums[r] == 1 or cnt0 < k):
            if nums[r] == 0:
                cnt0 += 1
            r += 1
        currlen = r - l
        while r + 1 < len(nums):
            # move r to next
            r += 1
            while r < len(nums) and nums[r] == 1:
                r += 1
            # move l to next
            while l < r and nums[l] == 1:
                l += 1
            l += 1
            currlen = max(currlen, r - l)
        return currlen
                