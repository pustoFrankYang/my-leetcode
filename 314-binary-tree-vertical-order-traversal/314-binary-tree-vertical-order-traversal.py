# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Q314m, runtime 90.65
# from mobile phone XD
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        c2v = {}
        q = []
        minc = 0
        if root:
            q.append((root, 0))
        while q:
            p, c = q.pop(0)
            minc = min(minc, c)
            if c in c2v:
                c2v[c].append(p.val)
            else:
                c2v[c] = [p.val]
            if p.left:
                q.append((p.left, c - 1))
            if p.right:
                q.append((p.right, c + 1))
        i = minc
        ans = []
        while i in c2v:
            ans.append(c2v[i])
            i += 1
        return ans

        