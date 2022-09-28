# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        curr = []
        tgt_rt = []
        def dfs_find(node):
            if node.val == target.val: ### val
                tgt_rt = curr.copy()
                return curr.copy()
            lres = rres = []
            if node.left:
                curr.append(node.left.val)
                lres = dfs_find(node.left)
                curr.pop()
            if node.right:
                curr.append(node.right.val)
                rres = dfs_find(node.right)
                curr.pop()
            return lres if lres else rres
        curr = []
        curr.append(root.val)
        tgt_rt = dfs_find(root)
        curr = []
        ans = []
        def dfs(node):
            dist = 0
            p = 0
            while p < len(curr) and p < len(tgt_rt) and curr[p] == tgt_rt[p]:
                p += 1
            # p -= 1
            dist = len(tgt_rt) - p + (len(curr) - p)
            # print(node.val, p, dist, curr)
            if dist == k:
                ans.append(node.val)
                # return
            if node.left:
                curr.append(node.left.val)
                dfs(node.left)
                curr.pop()
            if node.right:
                curr.append(node.right.val)
                dfs(node.right)
                curr.pop()
        curr.append(root.val)
        dfs(root)
        return ans