class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        u2v = defaultdict(list)
        for u, v in edges:
            u2v[u].append(v)
        if len(u2v[source]) <= 0:
            return source == destination  ###???
        # False when any path has loop or end not in desti
        vis = {}
        for u in u2v.keys():
            vis[u] = False
            for v in u2v[u]:
                vis[v] = False
        
        def dfs(n):
            if vis[n]:
                return False
            vis[n] = True
            if len(u2v[n]) <= 0 and n != destination:
                return False
            for v in u2v[n]:
                if dfs(v) == False:
                    return False
                vis[v] = False
            return True
        
        return dfs(source)
    
'''
1
[]
0
0
exp: true
'''