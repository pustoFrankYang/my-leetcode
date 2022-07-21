# Q71m, 32.59%
class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        for part in path.split('/'):
            if part == '..':
                if ans:
                    ans.pop()
            elif part == '':
                continue
            elif part != '.':
                ans.append(part)
        return '/' + '/'.join(ans)