# Q2348m, runtime
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        metas = []
        curr = 0
        for n in nums:
            if n == 0:
                curr += 1
            else:
                if curr >= 0:
                    metas.append(curr)
                    curr = 0
        if curr >= 0:
            metas.append(curr)
            curr = 0
        ans = 0
        for m in metas:
            ans += m *(1 + m) // 2
        return ans