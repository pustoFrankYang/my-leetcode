# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Q545m, runtime 10.58%, py
# !!! leaves should left to right, should DFS
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        ls, rs, leafs = [], [], []
        eol = TreeNode()
        q = []
        if root.right:
            q.append((root.right, 'r'))
        if root.left:
            q.append((root.left, 'l'))
        prev = None
        while q:
            curr, label = q.pop()
            if not curr.left and not curr.right:
                leafs.append(curr.val)
                continue
            if label == 'l':
                ls.append(curr.val)
                if curr.left:
                    if curr.right:
                        q.append((curr.right, None))
                    q.append((curr.left, 'l'))
                else:
                    q.append((curr.right, 'l'))
            elif label == 'r':
                rs.append(curr.val)
                if curr.right:
                    q.append((curr.right, 'r'))
                    if curr.left:
                        q.append((curr.left, None))
                else:
                    q.append((curr.left, 'r'))
            else:
                if curr.right:
                    q.append((curr.right, None))
                if curr.left:
                    q.append((curr.left, None))
        return [root.val] + ls + leafs + rs[::-1]
'''
WA
[1,2,7,3,5,null,6,4]
'''