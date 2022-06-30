# Q457, runtime 97.36%
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        visited = [0] * n
        for i in range(n):
            if visited[i]:
                continue
            # no visited, let's check cycle
            f = s = i
            while nums[(f + nums[f]) % n] * nums[f] > 0:
                endflg = False
                for _ in range(2):
                    f = (f + nums[f]) % n
                    visited[f] = 1
                    if nums[(f + nums[f]) % n] * nums[f] < 0:
                        endflg = True
                        break
                    elif f == s:
                        # length
                        if (f + nums[f]) % n != f: return True
                        else:
                            endflg = True
                            break    
                if endflg: break
                    
                s = (s + nums[s]) % n
        return False
        
'''
WA:
[-1,-2,-3,-4,-5]

# loop end indent wrong
[3,1,2]
'''