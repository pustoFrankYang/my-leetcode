class Solution:
    # ohhh i am not fluent in sliding window
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        minop = float('inf')
        p, q = 0, 0
        wind = 0
        while q < len(nums):
            while q < len(nums) and wind < target:
                wind += nums[q]
                q += 1
                
            if wind == target:
                minop = min(minop, len(nums) - (q - p))
            
            while p < q and wind > target:
                wind -= nums[p]
                p += 1
                
            if wind == target:
                minop = min(minop, len(nums) - (q - p))
            
            if q < len(nums):  ## to let it not infinite loop
                wind += nums[q]
                q += 1
                
        return minop if minop < float('inf') else -1