# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root, None]
        prev = None
        ans = []
        # BFS
        while q:
            curr = q.pop(0)
            if not curr:
                if prev != None:
                    ans.append(prev)
                    q.append(None)
                    prev = None
                else:
                    break
            else:
                prev = curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return ans