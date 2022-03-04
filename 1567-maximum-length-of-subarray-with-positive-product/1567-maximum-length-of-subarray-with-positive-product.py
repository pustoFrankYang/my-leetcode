# WA [5,-20,-20,-39,-5,0,0,0,36,-32,0,-7,-10,-7,21,20,-12,-34,26,2]
# WA [1000000000]
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        # dp positiv or nega, for subarr ending in i
        # now change dp into two var
        dpp = dpn = 0
        if nums[0] > 0:
            dpp = 1
        elif nums[0] < 0:
            dpn = 1
        maxdpp = dpp  #### WA [1000000000]
        for i in range(1, n):
            if nums[i] > 0:
                if dpn > 0:
                    dpp, dpn = dpp + 1, dpn + 1
                else:
                     dpp, dpn = dpp + 1, 0
            elif nums[i] < 0:
                if dpn > 0:
                    dpp, dpn = dpn + 1, dpp + 1
                else:
                    dpp, dpn = 0, dpp + 1
            else:
                dpp = dpn = 0
            maxdpp = max(maxdpp, dpp)
        return maxdpp