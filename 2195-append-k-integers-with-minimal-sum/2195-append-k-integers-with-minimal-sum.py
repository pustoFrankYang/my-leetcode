'''
MLE
[1]
100000000
'''
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums.append(float('inf'))
        prev = 0
        ans = 0
        for n in nums:
            if k <= 0:
                break
            if n > prev + 1:
                if n - prev - 1 <= k:
                    ans += (n - prev - 1) * (prev + n) // 2  # sum([x for x in range(prev + 1, n)])
                    k -= n - prev - 1
                else:
                    ans += k * (prev + 1 + prev + k) // 2  # sum([x for x in range(prev + 1, prev + 1 + k)])
                    k = 0
            prev = n
        return ans