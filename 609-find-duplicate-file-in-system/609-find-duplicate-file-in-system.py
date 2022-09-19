# Q609m, runtime 99.83%, py
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        cont2dirs = defaultdict(list)
        ans = []
        for info in paths:
            parts = info.split(' ')
            dire = parts[0]
            for file in parts[1:]:
                fn, cont = file.split('(')
                cont.strip(')')
                cont2dirs[cont].append(dire + '/' + fn)
        for cont, dirs in cont2dirs.items():
            if len(dirs) > 1:
                ans.append(dirs)
        return ans