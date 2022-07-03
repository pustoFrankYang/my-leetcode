# Q376m, 70.30%
class Solution:
    # greedy
    # just start from 1st element and change direc whenever it can change
    # say A, B, C
    # if A == B, then ans(A,B,C) == ans(B,C)
    # if A > B and B > C, then ans = 1
    # if A > B and B < C, then ans = 2
    # so always start with A for whatever sequence
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        prevdiff = nums[1] - nums[0]
        cnt = 1 if prevdiff == 0 else 2
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0):
                cnt += 1
                prevdiff = diff
        return cnt