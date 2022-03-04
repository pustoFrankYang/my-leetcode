'''
WA:
5
[2,3,1,1,1,1,1]
15
[1,2,3,4,5]
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p = q = currsum = 0  # [p, q)
        minlen = float('inf')
        while q < len(nums):
            currsum += nums[q]
            q += 1
            while q < len(nums) and currsum < target:
                currsum += nums[q]
                q += 1
            if currsum >= target:  ####
                minlen = min(minlen, q - p)
            while p < q and currsum - nums[p] >= target:
                currsum -= nums[p]
                p += 1
                minlen = min(minlen, q - p)
                # print(p, q, currsum)

        return minlen if minlen < float('inf') else 0