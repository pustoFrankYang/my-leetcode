# Q2007m, runtime 84.56%, py
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        ans = []
        if len(changed) % 2 == 1: return []
        changed.sort()
        odd2grp = defaultdict(dict)
        for n in changed:
            odd = n
            while odd != 0 and odd % 2 == 0:
                odd //= 2
            odd2grp[odd][n] = odd2grp[odd].get(n, 0) + 1
        for odd, grp in odd2grp.items():
            vals = list(grp.keys())
            vals.sort()
            ind = 0
            while ind < len(vals):
                p = vals[ind]
                if grp[p] <= 0: # skip cnt==0
                    ind += 1
                    continue
                if 2 * p not in grp:
                    return []
                if p == 0 and grp[2 * p] <= 1 or p >= 0 and grp[2 * p] <= 0:
                    return []
                grp[p] -= 1
                grp[2 * p] -= 1
                ans.append(p)
                if grp[p] <= 0:
                    ind += 1
        return ans
        