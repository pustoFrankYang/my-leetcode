# Q15m, runtime 68.05%
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        # iter i to find [i, j, k]
        for i in range(len(nums) - 2):
            if nums[i] >  0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while r >= 0 and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return ans