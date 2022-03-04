'''
WA
"eeccccbebaeeabebccceea"
"aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        p = 0
        q = len(s) - 1
        deleted = 0
        def validPalindromeStrict(s):
            p = 0
            q = len(s) - 1
            
            while p < q:
                if s[p] != s[q]:
                    return False
                p += 1
                q -= 1
            return True
        
        while p < q:
            if s[p] != s[q]:
                if deleted:
                    print(p, s[p], q, s[q], len(s))
                    return False
                else:
                    return validPalindromeStrict(s[p+1:q+1]) or validPalindromeStrict(s[p:q])
            p += 1
            q -= 1
        return True