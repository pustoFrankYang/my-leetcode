class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        t = 0
        for i in range(len(nums)):
            t += nums[i]
            ans[i] = t
        return ans