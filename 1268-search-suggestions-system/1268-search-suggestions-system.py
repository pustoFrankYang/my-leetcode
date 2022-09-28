
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    
        class Node:
            def __init__(self, val, next=[None] * 26, isWord=False):
                self.val = val
                self.next = next
                self.isWord = isWord ####
                
        head = Node(' ', [None] * 26, False)
        curr = head
        for prod in products:
            curr = head
            for ch in prod:
                ind = ord(ch) - ord('a')
                if curr.next[ind] is not None:
                    curr = curr.next[ind]
                else:
                    curr.next[ind] = Node(ch, [None] * 26, False)
                    curr = curr.next[ind]
            curr.isWord = True
            
        ans = []
        
        def dfs(node, currstr):
            ans = []
            if node is None:
                return []
            if node.isWord: # 在这里加，以防漏掉第一个词
                ans.append(currstr)
            for kid in node.next:
                if kid:
                    ans += dfs(kid, currstr + kid.val)
            return ans
        
        curr = head
        currstr = ""
        for ch in searchWord:
            currstr += ch
            if curr is None:
                ans.append([])
            else:
                curr = curr.next[ord(ch) - ord('a')]
                t = dfs(curr, currstr)
                ans.append(t[:3])
        return ans