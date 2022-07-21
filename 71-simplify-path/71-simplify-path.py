# Q71m, 91.13%
class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        for part in path.split('/'):
            if part == '..':
                if ans:  # cuz [] can't pop()
                    ans.pop()
            elif part == '':
                continue
            elif part != '.':
                ans.append(part)
        return '/' + '/'.join(ans)