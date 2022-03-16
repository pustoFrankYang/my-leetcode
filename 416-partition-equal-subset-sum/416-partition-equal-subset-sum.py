'''
RE
[1,2,5]
[100]
[9,5]

WA
[14,9,8,4,3,2]
[1,5,10,6]
'''
class Solution:
    # reviewing 0-1 bag
    def canPartition(self, nums: List[int]) -> bool:
        summer = sum(nums)
        if summer % 2 == 1 or len(nums) <= 1:
            return False
        target = summer // 2
        # dp[i][w] first elements max. i to sum w ma
        dp = [[False] * (target + 1) for _ in range(len(nums))]
        if nums[0] <= target:  ####
            dp[0][nums[0]] = True
        for i in range(1, len(nums)):
            if nums[i] > target:  ####
                continue
            dp[i][nums[i]] = True
            for w in range(target + 1):
                dp[i][w] = dp[i][w] or dp[i - 1][w - nums[i]] or dp[i - 1][w]  ########
            if dp[i][target]:  ##
                return True
        # print(dp)
        return False