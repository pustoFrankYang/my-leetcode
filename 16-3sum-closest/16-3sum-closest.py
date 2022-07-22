# Q16m, runtime 12.63%
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = sum(nums[:3])  #!!! caution
        # iter i to find [i, j, k]
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                isum = nums[i] + nums[l] + nums[r]
                if isum == target:
                    return target
                elif isum < target:
                    l += 1
                else:
                    r -= 1
                ans = ans if abs(ans - target) < abs(isum - target) else isum
        return ans
    
'''
[0,1,2]
0
'''
