class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # begin point to end point, got from edges
        u2v = [[] for _ in range(n)]
        # ancestors alle
        ans = [[] for _ in range(n)]
        # cnt of prev points not processed
        prevcnt = [0] * n
        # queue of no-prev points
        q = []
        
        for u, v in edges:
            u2v[u].append(v)
            prevcnt[v] += 1
        for i in range(n):
            if prevcnt[i] == 0:
                q.append(i)
        
        # popped element u inject itself to ans[v]
        while q:
            u = q.pop(0)
            for v in u2v[u]:  ## inject its ancestors to EVERY succeeders
                for ances in ans[u]:
                    if ances not in ans[v]:
                        ans[v].append(ances)
            for v in u2v[u]:
                ans[v].append(u)
                prevcnt[v] -= 1
                if prevcnt[v] == 0:
                    q.append(v)
        
        return [sorted(x) for x in ans]