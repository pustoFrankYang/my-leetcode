class Solution:
    
    # !!! 1e9+7 是浮点数，而 1000000007 是整型，不一样。。。
    def numOfWays(self, nums: List[int]) -> int:
        def f(nums: List[int]) -> int:
            if len(nums) <= 2:
                return 1
            lessers = [x for x in nums if x < nums[0]]
            greaters = [x for x in nums if x > nums[0]]
            return f(lessers) * f(greaters) * comb(len(nums) - 1, len(lessers)) % (1000000007)
    
        return (f(nums) - 1) % (1000000007)