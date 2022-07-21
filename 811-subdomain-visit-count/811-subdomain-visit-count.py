# Q811m, 91.99%
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        m = {}
        for s in cpdomains:
            cnt, do = s.split(' ')
            cnt = int(cnt)
            dos = do.split('.')
            m[dos[-1]] = m.get(dos[-1], 0) + cnt
            m[dos[-2] + '.' + dos[-1]] = m.get(dos[-2] + '.' + dos[-1], 0) + cnt
            if len(dos) == 3:
                m[dos[-3] + '.' + dos[-2] + '.' + dos[-1]] = m.get(dos[-3] + '.' + dos[-2] + '.' + dos[-1], 0) + cnt
        ans = []
        for k, v in m.items():
            ans.append(str(v) + ' ' + k)
        return ans