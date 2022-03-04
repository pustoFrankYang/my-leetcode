# WA [5,-20,-20,-39,-5,0,0,0,36,-32,0,-7,-10,-7,21,20,-12,-34,26,2]
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        # dp positiv or nega, for subarr ending in i
        dpp = [0] * n
        dpn = [0] * n
        if nums[0] > 0:
            dpp[0] = 1
        elif nums[0] < 0:
            dpn[0] = 1
        for i in range(1, n):
            if nums[i] > 0:
                dpp[i] = dpp[i - 1] + 1
                dpn[i] = dpn[i - 1] + 1 if dpn[i - 1] > 0 else 0
            elif nums[i] < 0:
                dpp[i] = dpn[i - 1] + 1 if dpn[i - 1] > 0 else 0  #### forgot
                dpn[i] = dpp[i - 1] + 1
            else:
                dpp[i] = dpn[i] = 0
        return max(dpp)