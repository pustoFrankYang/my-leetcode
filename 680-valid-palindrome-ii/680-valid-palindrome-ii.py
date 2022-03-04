'''
WA
"eeccccbebaeeabebccceea"
"aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        
        def validPalindromeStrict(s):
            p = 0
            q = len(s) - 1
            
            while p < q:
                if s[p] != s[q]:
                    return False
                p += 1
                q -= 1
            return True
        
        
        p = 0
        q = len(s) - 1
        deleted = 0
        while p < q:
            if s[p] != s[q]:
                #### it is hard to write without aux func... so
                return validPalindromeStrict(s[p+1:q+1]) or validPalindromeStrict(s[p:q])
            p += 1
            q -= 1
        return True