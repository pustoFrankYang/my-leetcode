# Q922e, runtime 83.70%
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        p, q = -1, -1
        cur = 0
        ans = [0] * len(nums)
        while cur < len(nums):
            p += 1
            while nums[p] % 2 == 1:
                p += 1
            ans[cur] = nums[p]
            cur += 1
            
            q += 1
            while nums[q] % 2 == 0:
                q += 1
            ans[cur] = nums[q]
            cur += 1
        return ans
