'''
WA
[2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2]
3
oupu: 9
expe: 4
'''
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d2cnt = {}
        ans = 0
        for n in nums:
            d2cnt[n] = d2cnt.get(n, 0) + 1
        for n in nums:
            if k - n != n and d2cnt.get(k - n, 0) and d2cnt[n]:  # !! 
                d2cnt[k - n] -= 1
                d2cnt[n] -= 1
                ans += 1
            if k - n == n and d2cnt[n] >= 2:
                d2cnt[n] -= 2
                ans += 1
        return ans