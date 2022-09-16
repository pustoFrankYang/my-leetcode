# Q1152m, runtime 79.78%, py
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # {pattern -> [usernames]}
        p2u = defaultdict(set)
        # user -> indexes
        u2i = defaultdict(list)
        for i in range(len(username)):
            u2i[username[i]].append(i)
        for u, inds in u2i.items():
            inds = sorted(inds, key=lambda x : timestamp[x]) # !!! timestamp
            webs = list(website[i] for i in inds)
            n = len(webs)
            if n < 3:
                continue
            for a in range(n - 2):
                for b in range(a + 1, n - 1):
                    for c in range(b + 1, n):
                        p2u[str([webs[a], webs[b], webs[c]])].add(u)
        maxs = 0
        ps = []
        for p, uns in p2u.items():
            if len(uns) > maxs:
                maxs = len(uns)
                ps = [p]
            elif len(uns) == maxs:
                ps.append(p)
        # change str repre of list into list
        return sorted(ps)[0].replace("'", "").strip('[]').split(', ')