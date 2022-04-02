'''
TLE:
"..........." too long
'''
class Solution:
    def numberOfWays(self, s: str) -> int:
        # ¡¡¡gesah!!! WO RI NI MA! you canns machen dadurch, du BOTH prefix UND suffix count!!!!!!!!
                
        pre0 = [0] * len(s)
        pre1 = [0] * len(s)
        suf0 = [0] * len(s)
        suf1 = [0] * len(s)
        ans = 0
        
        for i in range(len(s)):
            if i == 0:
                if s[i] == '0':
                    pre0[i] += 1
                else:
                    pre1[i] += 1
            else:
                if s[i] == '0':
                    pre0[i] = pre0[i - 1] + 1
                    pre1[i] = pre1[i - 1]
                else:
                    pre1[i] = pre1[i - 1] + 1
                    pre0[i] = pre0[i - 1]
                    
        for i in reversed(range(len(s))):
            if i == len(s) - 1:
                if s[i] == '0':
                    suf0[i] += 1
                else:
                    suf1[i] += 1
            else:
                if s[i] == '0':
                    suf0[i] = suf0[i + 1] + 1
                    suf1[i] = suf1[i + 1]
                else:
                    suf1[i] = suf1[i + 1] + 1
                    suf0[i] = suf0[i + 1]
                    
        for i in range(len(s)):
            if s[i] == '0':
                ans += pre1[i] * suf1[i]
            else:
                ans += pre0[i] * suf0[i]
                
        return ans
            
        
        return ans