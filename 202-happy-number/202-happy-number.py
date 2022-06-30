class Solution:
    def isHappy(self, n: int) -> bool:
        def n2hp(x):
            ans = 0
            for digit in str(x):
                ans += int(digit) **2
            return ans
        
        # fast & slow pnt to detect cycle
        f = s = n 
        while f != 1:
            f = n2hp(f)
            if f == 1: return True
            elif f == s: return False
            
            f = n2hp(f)
            if f == 1: return True
            elif f == s: return False
            
            s = n2hp(s)
            
        return True