# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        rootv = set(e[0] for e in descriptions)
        u2v_isLeft = defaultdict(list)
        for d in descriptions:
            rootv.discard(d[1])
            u2v_isLeft[d[0]].append((d[1], d[2]))
        root = TreeNode(min(rootv))
        q = [root]
        while q:
            curr = q.pop(0)
            for v, isLeft in u2v_isLeft[curr.val]:
                
                if isLeft:
                    curr.left = TreeNode(v)
                    q.append(curr.left)
                else:
                    curr.right = TreeNode(v)
                    q.append(curr.right)
        return root